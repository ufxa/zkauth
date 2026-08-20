# Ciclo 01 — Response to Reviewers

## C-001 — Figuras não rastreáveis aos dados
**Reviewer Comment:** valores das Figs. 4-6 divergem de data/results/*.csv; error bars
da Fig. 6 sem variância medida.
**Author Response:** Concordamos. Causa-raiz: as coordenadas das figuras haviam sido
transcritas de valores aproximados de literatura, não extraídas dos CSVs; e a seção de
escalabilidade da simulação produzia 1 amostra por ponto (sem variância).
**Changes Made:**
1. `src/evaluation/run_simulation.py`: seção de escalabilidade reescrita com 10
   repetições por célula (scale × scheme), gerando `verify_ms_std/ci95` e
   `ppas_std/ci95` medidos. Simulação reexecutada (seed=42); `raw_rounds.csv` e
   `aggregate_ppas.csv` permanecem byte-idênticos (reseed por rodada preserva o
   stream RNG); `scalability.csv` e `attack_resistance.csv` regenerados.
2. Fig. 4 (main.tex ~linha 1130): coordenadas por rodada extraídas de
   `raw_rounds.csv` com IC95 = t·std/√1000 (5 casas decimais).
3. Fig. 5 (~linha 1215): 16 barras extraídas de `attack_resistance.csv` (em %).
4. Fig. 6 (~linha 1300): 4 séries × 2 subplots extraídas de `scalability.csv`
   com IC 95% medido; ymax 180→200 (Bulletproofs 180.2 ms a 10^5).
5. Prosa dependente (§VI.E): "≈29%"→"≈98% (44.8→88.4 ms)"; Bulletproofs
   "45.6%"→"51.8%, cruzando V_max=120 ms em todas as escalas"; adicionada a
   queda do ZK-STARK PPAS 0.843→0.696.
6. Comentários no fonte TikZ apontando o arquivo de dados de cada figura.

## M-001 — Acknowledgment Bloco 2 não literal
**Author Response:** Concordamos. **Changes Made:** bloco substituído pelo texto
literal da Fase 1 (incluindo grafia original), main.tex §Acknowledgment.

## M-002 — src/ e notebooks/ vazios
**Author Response:** Concordamos. **Changes Made:** criados
`src/metrics/ppas.py`, `src/agents/{prover,verifier,registry}_agent.py` (+__init__),
`src/evaluation/run_simulation.py` (driver canônico, sanitizado do script de HPC),
`notebooks/reproduce_figures.ipynb` (reproduz Figs. 4-6 dos CSVs) e
`paper/figures/README.md`. Verificação: `python3 src/evaluation/run_simulation.py`
reproduziu os 6 arquivos de resultado; antes da alteração da escalabilidade, a
reprodução foi confirmada byte-idêntica aos CSVs publicados (diff vazio).

## M-003 — Travessões em prosa
**Author Response:** Concordamos. **Changes Made:** linhas 190-191 e 1394
(parênteses/vírgula), 1457-1459 (parênteses), rótulos de fase da Fig. 2 ("---"→":").
Ocorrências restantes de "--"/"—" estão apenas em comentários LaTeX e sintaxe TikZ.

## m-001/m-002/m-003 — reconhecidos; desvios documentados em phase_1_invariants.md.
