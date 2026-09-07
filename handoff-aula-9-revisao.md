# Handoff: revisão da Aula 9 (Portfólio e CAPM)

Prompt para uma sessão local, na máquina onde está o `.qmd` da aula e a cadeia Quarto + decktape.
Cole o bloco abaixo inteiro como primeira mensagem.

---

## Contexto

Estou revisando a Aula 9 do curso de Finanças (graduação), hoje intitulada "Revisão: Portfólio, CAPM e APT". O fonte é o `.qmd` desta aula neste repositório; a versão publicada está em `financas-graduacao/9-portfolio-capm-apt/index.html` (reveal.js gerado pelo Quarto 1.8) e no PDF ao lado, gerado com decktape.

A aula é uma **revisão** para alunos que sabem matemática e estatística bem. Objetivos da revisão:

1. Passar mais rápido pelo básico.
2. Mostrar alguns resultados mais formalmente: linearidade dos retornos nos pesos **em toda realização**, linearidade do valor esperado como consequência, comportamento de média e variância nos pesos.
3. Trocar figuras estáticas por artefatos interativos (SVG + JavaScript inline, sem bibliotecas), no padrão que as Aulas 6 e 7 já usam.
4. Substituir a derivação heurística do CAPM por uma derivação curta e fechada, com o caso geral num apêndice.

As decisões abaixo já foram tomadas; não reabra. Onde houver dúvida de detalhe, escolha a opção mais simples e me avise no resumo final.

## Decisões fechadas

| Tema | Decisão |
|---|---|
| Título | "Revisão: Portfólio e CAPM" (tirar APT; não há conteúdo de APT no deck) |
| Exemplos de pesos (1 a 4) | Manter como estão |
| Slides de distribuição, percentis e "Medindo risco" | Cortar (ids `medindo-o-retorno-uma-variável-aleatória` e `medindo-risco`, com as figuras `cell-3` e `cell-5`) |
| Exemplo Intel/ATP e solução | Cortar (ids `exemplo-intel-e-atp-oil-and-gas` e `solução`); substituir por um exemplo de uma linha no slide da linearidade |
| Tabela de combinações Intel/Coca-Cola e "eficiente vs. ineficiente" | Substituir pelo artefato de dois ativos (ids `retorno-x-volatilidade-das-combinações`, `gráfico-fronteira-de-dois-ativos`, `portfólio-eficiente-vs.-ineficiente`, `o-efeito-da-correlação`, `vendas-a-descoberto-short-sales`) |
| Formalização | Espaço de estados finito, depois caso geral em **somatórios**. Nada de notação vetorial no deck inteiro (sem `x'Σx`). |
| Derivação do CAPM no corpo | Perturbação `R_P + ε(R_i − r_f)`, duas derivadas em `ε = 0`, tudo em somatórios |
| Caso geral | Lagrangeano num **apêndice** ao final, em somatórios, com link a partir do slide da derivação |
| Artefatos | Quatro: (i) correlação e fronteira de 2 ativos; (ii) diversificação vs. n; (iii) carteira tangente e CML; (iv) Sharpe marginal e SML |
| Resto do deck | Ordem e conteúdo mantidos, salvo ajustes de texto para consistência de notação |

## Novos slides: conteúdo matemático

Use `R_i(s)` para o retorno do ativo `i` no estado `s`, probabilidades `π_s`, pesos `x_i` com `Σ_i x_i = 1`, `μ_i = E[R_i]`, `σ_ij = Cov(R_i, R_j)`, `σ_i² = σ_ii`, `ρ_ij = σ_ij/(σ_i σ_j)`.

### Slide A: linearidade em toda realização (substitui "Medindo o retorno esperado")

Tabela pequena: 3 estados × 2 ativos, com coluna `R_p(s)` calculada.

- Em **cada** estado `s`, a riqueza final é `W_0 Σ_i x_i (1 + R_i(s))`, logo `R_p(s) = Σ_i x_i R_i(s)`. Isso é uma identidade entre variáveis aleatórias; não usa probabilidade nenhuma.
- Consequência imediata: `E[R_p] = Σ_s π_s R_p(s) = Σ_s π_s Σ_i x_i R_i(s) = Σ_i x_i Σ_s π_s R_i(s) = Σ_i x_i μ_i`. A troca de somas é o único passo; `E` é linear porque é uma soma ponderada.
- Exemplo de uma linha: R$ 25 mil a 18% e R$ 35 mil a 25% ⇒ `0,4167·18% + 0,5833·25% = 22,1%`.

### Slide B: variância é quadrática nos pesos

- `R_p − E[R_p] = Σ_i x_i (R_i − μ_i)` (mesma identidade, centrada).
- `Var(R_p) = E[(Σ_i x_i (R_i − μ_i))²] = Σ_i Σ_j x_i x_j E[(R_i − μ_i)(R_j − μ_j)] = Σ_i Σ_j x_i x_j σ_ij`.
- Observações: (a) é uma forma quadrática nos pesos; é `≥ 0` para todo `x` porque é uma variância, o que é exatamente dizer que a matriz `[σ_ij]` é semidefinida positiva; (b) `SD(R_p) ≤ Σ_i |x_i| σ_i`, com igualdade se e só se todos os pares têm `ρ_ij = 1` (desigualdade triangular para desvios-padrão).
- Contraste visual no mesmo slide: média é **reta** em `x`, variância é **parábola** em `x`.

### Slide C: dois ativos (acompanha o artefato i)

- `μ_p = x μ_1 + (1 − x) μ_2`
- `σ_p² = x² σ_1² + (1 − x)² σ_2² + 2x(1 − x) ρ σ_1 σ_2`
- Casos-limite a exibir no artefato: `ρ = 1` dá `σ_p = |x σ_1 + (1 − x) σ_2|` (reta); `ρ = −1` dá variância zero em `x = σ_2/(σ_1 + σ_2)`; mínimo de variância em geral em `x* = (σ_2² − ρ σ_1 σ_2)/(σ_1² + σ_2² − 2ρ σ_1 σ_2)`.

### Slide D: pesos iguais (já existe; só conferir a notação)

`Var(R_p) = (1/n)·σ̄² + (1 − 1/n)·σ̄_ij`, com `σ̄²` a média das variâncias e `σ̄_ij` a média das covariâncias fora da diagonal. Limite `n → ∞`: `σ̄_ij`. Exemplo numérico existente: `√(0,4·0,1·0,1) = 6,3%`.

### Slide E: derivação do CAPM por perturbação (substitui os três slides "Aumentando o índice de Sharpe", "Quando vale a pena adicionar i" e "Beta de i em relação a P")

Partindo de uma carteira arriscada `P`, tome emprestado `ε` à taxa `r_f` e invista em `i`:

- `R(ε) = R_P + ε(R_i − r_f)`
- `μ(ε) = μ_P + ε(μ_i − r_f)` ⇒ `dμ/dε = μ_i − r_f`
- `σ²(ε) = σ_P² + 2ε Cov(R_i, R_P) + ε² σ_i²` ⇒ `dσ/dε|_{ε=0} = Cov(R_i, R_P)/σ_P = σ_i ρ_iP`

Isso **prova** a afirmação que hoje está solta no deck ("a volatilidade sobe apenas por `SD(R_i)·Corr(R_i, R_P)`").

Índice de Sharpe `S(ε) = (μ(ε) − r_f)/σ(ε)`:

- `S'(0) = [(μ_i − r_f) − S_P · σ_i ρ_iP] / σ_P`
- `S'(0) > 0` ⟺ `μ_i − r_f > S_P · σ_i ρ_iP` (é o "Sharpe marginal" do deck atual, agora derivado)
- Como `ε` pode ser negativo (vender `i`), `P` só tem Sharpe máximo se `S'(0) = 0` **para todo** `i`:

`μ_i − r_f = β_i^P (μ_P − r_f)`, com `β_i^P = Cov(R_i, R_P)/σ_P² = σ_i ρ_iP / σ_P`

Checagens de consistência que valem um bullet: `β_P^P = 1`; `Σ_i x_i β_i^P = 1` (bilinearidade da covariância).

Slide seguinte mantém o texto atual "Portfólio eficiente e retorno exigido", agora como corolário, com link: "a demonstração de que a condição vale para todos os `i` simultaneamente está no apêndice".

### Apêndice: caso geral por lagrangeano (em somatórios)

Problema: maximizar `Σ_i w_i (μ_i − r_f)` sujeito a `Σ_i Σ_j w_i w_j σ_ij = σ̄²`.

- Lagrangeano: `L = Σ_i w_i (μ_i − r_f) − (λ/2)(Σ_i Σ_j w_i w_j σ_ij − σ̄²)`
- CPO para cada `k`: `μ_k − r_f = λ Σ_j σ_kj w_j = λ Cov(R_k, R_w)`
- Multiplique por `w_k` e some em `k`: `μ_w − r_f = λ σ_w²`, logo `λ = (μ_w − r_f)/σ_w²`
- Substitua: `μ_k − r_f = [Cov(R_k, R_w)/σ_w²](μ_w − r_f) = β_k^w (μ_w − r_f)` para todo `k`

Comentários: (a) a CPO é um sistema linear `Σ_j σ_kj w_j ∝ μ_k − r_f`; é assim que o artefato (iii) calcula a carteira tangente (resolve e normaliza para somar 1); (b) no exemplo da aula as correlações são zero, então `w_i ∝ (μ_i − r_f)/σ_i²`, o que dá 51,0% / 40,8% / 8,2% com `r_f = 1%`; (c) a mesma condição sai de maximizar o Sharpe diretamente, porque o Sharpe é homogêneo de grau zero em `w`.

O restante (expectativas homogêneas + equilíbrio de mercado ⇒ `P = M`, CML, SML, beta de portfólio, alfa) fica como está.

## Artefatos interativos

Padrão: copiar a estrutura das Aulas 6 e 7 (ver `7-orcamento-capital/index.html` publicado, bloco `<style>` com prefixo `a7r` e helpers `a7rFmt`, `a7rMulberry32`). No `.qmd`, cada artefato entra num bloco `{=html}` dentro do slide, com CSS e JS inline, prefixo `a9p`, sem CDN. Cada artefato mostra números formatados em português (vírgula decimal) e tem casos-limite visíveis.

Parâmetros do exemplo da aula, a reutilizar em todos: Intel (26%, 50%), Coca-Cola (6%, 25%), Bore (2%, 25%), correlações zero, `r_f = 1%`.

### (i) Correlação e fronteira de dois ativos

- Controles: slider `ρ ∈ [−1, 1]`, passo 0,05; toggle "permitir vendas a descoberto" (estende `x` para `[−0,5, 1,5]`).
- Desenho: plano (σ, μ) com a curva das combinações, os dois ativos marcados, o ponto de variância mínima destacado, e a reta `ρ = 1` tracejada como referência fixa.
- Painel: `x*` de variância mínima, `σ_p` em `x*`, e a frase "com `ρ = −1` a variância zera em `x = σ_2/(σ_1+σ_2)`" quando `ρ = −1`.
- Substitui a tabela de combinações, "eficiente vs. ineficiente" (mostrar com um marcador em `x = 0,2` que domina 100% Coca-Cola: 10,0% vs 6,0% de retorno, 22,4% vs 25,0% de vol; com `ρ = 0`, `x = 0,2` é exatamente o ponto de variância mínima, `x* = σ_2²/(σ_1² + σ_2²)`), "efeito da correlação" e "vendas a descoberto".

### (ii) Diversificação vs. n

- Controles: sliders para vol média `σ̄ ∈ [5%, 30%]` e correlação média `ρ̄ ∈ [0, 1]`; `n` no eixo horizontal de 1 a 100 (escala log opcional).
- Desenho: `σ_p(n) = √(σ̄²/n + (1 − 1/n) ρ̄ σ̄²)` e a assíntota `σ̄ √ρ̄` tracejada.
- Painel: `σ_p` em `n = 1, 10, 30, 100` e no limite; destacar que com `ρ̄ = 0` o limite é zero e com `ρ̄ = 1` a curva é plana.

### (iii) Carteira tangente e CML

- Controles: slider `r_f ∈ [0%, 5%]`; toggle "vendas a descoberto".
- Desenho: fronteira de variância mínima dos três ativos (com short: hipérbole calculada analiticamente; sem short: varrer simplex numa grade), ponto tangente, reta CML, os três ativos.
- Cálculo da tangente com short: resolver `Σ_j σ_kj w_j = μ_k − r_f` e normalizar. Sem short: busca em grade no simplex maximizando Sharpe (grade de 1%).
- Painel: pesos, `E[R_M]`, `SD(R_M)`, Sharpe. Com `r_f = 1%` deve reproduzir 51,0% / 40,8% / 8,2%, `E = 15,9%`, `SD = 27,6%`.

### (iv) Sharpe marginal e SML

- `P` fixo = carteira tangente com `r_f = 1%`. Um quarto ativo hipotético `i` com sliders `μ_i ∈ [0%, 30%]`, `σ_i ∈ [10%, 60%]`, `ρ_iP ∈ [−1, 1]`.
- Painel esquerdo: curva `S(ε)` para `ε ∈ [−0,5, 0,5]`, com a reta tangente em `ε = 0` e o sinal de `S'(0)` em destaque.
- Painel direito: SML com os três ativos da aula sobre a reta e o ativo `i` marcado; `α_i = μ_i − [r_f + β_i^P (μ_P − r_f)]` exibido, com `β_i^P = σ_i ρ_iP / σ_P`.
- Mensagem: `α_i > 0` ⟺ `S'(0) > 0` ⟺ vale comprar `i`; `α_i = 0` coloca `i` exatamente na SML e a tangente em `ε = 0` fica horizontal.
- Acompanha o slide E.

Opcional, se couber no tempo: um mini-artefato no slide A com slider em `x` (dois ativos, três estados) recalculando a coluna `R_p(s)`, `E[R_p]` e `Var(R_p)` ao vivo, mostrando a reta e a parábola.

## Validação antes de publicar

1. Casos-limite de cada artefato: `ρ = 1` (reta), `ρ = −1` (variância zero), `ρ̄ = 0` e `ρ̄ = 1` em (ii), `r_f` variando em (iii) move o ponto tangente ao longo da fronteira, `α_i = 0` em (iv) dá tangente horizontal.
2. Números do exemplo: pesos 51,0 / 40,8 / 8,2; `E[R_M] = 15,9%`; `SD = 27,6%`; betas 1,68 / 0,34 / 0,07 (todos reconferidos: as três ações caem exatamente na SML e `Σ x_i β_i = 1`).
3. Renderizar com `quarto render`, abrir no navegador e passar por todos os slides; conferir que MathJax renderiza os somatórios e que nenhum artefato quebra o layout vertical (usar classe `smaller` quando preciso).
4. Gerar o PDF com decktape; artefatos aparecem no estado inicial, o que é aceitável.
5. Publicar copiando `index.html`, `index_files/` e o PDF para `financas-graduacao/9-portfolio-capm-apt/`, com commit "Atualiza Aula 9 (<hash do fonte>)", seguindo o padrão dos commits anteriores.

## Resumo final que espero

Tabela "slide antes → slide depois" com o que foi cortado, substituído e criado; lista dos casos-limite testados com o resultado; qualquer ponto onde você se afastou deste plano e por quê.
