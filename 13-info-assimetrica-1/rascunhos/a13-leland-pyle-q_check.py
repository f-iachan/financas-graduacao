"""Leland-Pyle (Tirole p.260): fração retida s*(q) que separa o tipo bom.
Contrato do bom na sua reta de lucro zero: R_e^F = pR(1-s), R_e^S = pR(1-s)+sR.
IC do ruim (seguro pleno em qR): q U(R_e^S) + (1-q) U(R_e^F) = U(qR)."""
import numpy as np

def brentq(f, a, b, args=(), xtol=1e-14):   # bisseção simples (sem scipy)
    fa = f(a, *args)
    for _ in range(200):
        m = 0.5*(a+b); fm = f(m, *args)
        if (fm > 0) == (fa > 0): a, fa = m, fm
        else: b = m
        if b - a < xtol: break
    return 0.5*(a+b)

def contrato(s, p, R):
    F = p*R*(1-s)
    return F, F + s*R

def ic_gap(s, q, p, R, U):           # >0: ruim ainda imita
    F, S = contrato(s, p, R)
    return q*U(S) + (1-q)*U(F) - U(q*R)

def s_star(q, p, R, U):
    return brentq(ic_gap, 0.0, 1-1e-12, args=(q, p, R, U), xtol=1e-14)

ln = np.log
crra = lambda g: (lambda x: np.log(x) if g == 1 else (x**(1-g)-1)/(1-g))
cara = lambda a: (lambda x: -np.exp(-a*x))

p, R = 0.7, 10.0
for q in [0.4, 0.3, 0.2, 0.1, 0.05]:
    s = s_star(q, p, R, ln); F, S = contrato(s, p, R)
    CE = np.exp(p*ln(S)+(1-p)*ln(F))
    print(f"q={q:.2f}  s*={s:.4f}  b=R_e^F={F:.3f} (<qR={q*R:.1f})  R_e^S={S:.3f}  "
          f"lb 1-q/p={1-q/p:.3f}  EC bom={CE:.3f} (pR={p*R})  custo={p*R-CE:.3f}")

# 1) monotonicidade em q para várias U côncavas e vários p
qs = np.linspace(0.01, 0.69, 300)
for name, U in [("ln", ln), ("CRRA 0.5", crra(0.5)), ("CRRA 3", crra(3)),
                ("CARA 0.1", cara(0.1)), ("CARA 1", cara(1.0)), ("sqrt", np.sqrt)]:
    ss = np.array([s_star(q, p, R, U) for q in qs])
    mono = np.all(np.diff(ss) < 0)
    lb = np.all(ss > 1 - qs/p - 1e-12)
    print(f"{name:9s} s* decrescente em q: {mono};  s*>1-q/p: {lb};  "
          f"s*(0.01)={ss[0]:.3f}  s*(0.69)={ss[-1]:.3f}")

# 2) limites: q->p => s*->0 ; risco-neutro => só s=1 separa
print("q=0.6999:", s_star(0.6999, p, R, ln))
# 3) invariância a R com log (CRRA): s* não depende de R
print("R=1 vs R=100 (q=.4):", s_star(.4, p, 1.0, ln), s_star(.4, p, 100.0, ln))
