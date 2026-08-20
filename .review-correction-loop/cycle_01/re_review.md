# Ciclo 01 — Re-review (academic-paper-reviewer, modo re-review, read-only)

## Matriz de verificação

| ID | Alegação do autor | Verificação material | Veredicto |
|----|-------------------|----------------------|-----------|
| C-001 | Figs 4-6 extraídas dos CSVs; escalabilidade com 10 reps/ponto e IC medido | Spot-checks: Fig.5 Groth16 Replay 1.88±0.52 == CSV 1.88±0.52; Fig.4 ZKAuth rodada 1 = 0.99242±0.00007 == raw_rounds.csv; Fig.6 STARK 10^5 = 88.40±0.70 == scalability.csv; prosa §VI.E atualizada (≈98%, 51.8%, 0.843→0.696); simulação reexecutada com sucesso; código com 10 reps confere | **FULLY_ADDRESSED** |
| M-001 | Bloco 2 substituído pelo texto literal | comparação fragmento-a-fragmento (7/7 presentes, incl. grafia literal "end Smart") | **FULLY_ADDRESSED** |
| M-002 | src/ + notebooks/ populados e funcionais | `python3 src/evaluation/run_simulation.py` executa e regenera resultados; reprodução byte-idêntica confirmada antes da mudança de escalabilidade; notebook cobre Figs 4-6 com IC | **FULLY_ADDRESSED** |
| M-003 | Travessões removidos da prosa | grep global: 0 ocorrências fora de comentários/sintaxe TikZ | **FULLY_ADDRESSED** |

## Regressões e novos achados
- Compilação tectonic: PASS (0 erros; PDF 178.7 KB, 16 páginas, inspeção visual das
  páginas das Figs. 4-6 sem overflow/sobreposição).
- Invariantes P1: nenhum regrediu (matriz revalidada; P1-004 permanece PARTIAL
  documentado — desvio de idade de referências, pré-existente e justificado).
- Segurança: git status sem codeA100/, sem segredos nos arquivos novos.
- Nenhum novo CRITICAL ou MAJOR.

## Decisão editorial do re-review: **ACCEPT (Minor)** — itens menores residuais
(m-001 idade de referências, m-003 overfull ≤5.5pt) registrados e não mascaram
nenhum requisito crítico.
