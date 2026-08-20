# Invariantes da Fase 1 (extraídos de Fase_1_BASE_PROMPT_ARTIGOS.md)

| ID | Requisito | Verificação | Status |
|----|-----------|-------------|--------|
| P1-001 | Tabelas: tabularx+booktabs, largura total, caption acima | inspeção main.tex + PDF | PASS |
| P1-002 | Sem " -- " / "—" em prosa | grep | PASS (corrigido ciclo 01) |
| P1-003 | ≥40 referências com DOI, indexadas | contagem: 59; 2 sem DOI são standards W3C/IETF com identificador formal | PASS |
| P1-004 | Máx. 20% refs pré-2023 | 24/59 = 41% | PARTIAL (desvio documentado: primitivas criptográficas fundacionais — Groth16 2016, GMR 1989, Bulletproofs 2018, Pippenger 1980 — são insubstituíveis) |
| P1-005 | Nenhuma ref exclusivamente arXiv/TechRxiv | grep: 0 | PASS |
| P1-006 | 6 figuras obrigatórias | Figs 1-6 presentes | PASS |
| P1-007 | Captions de figuras ACIMA | script de verificação: 6/6 | PASS |
| P1-008 | Figs 4-6 com IC 95% + desvio | error bars derivados de data/results (ciclo 01) | PASS |
| P1-009 | Pseudocódigo + métrica novel + complexidade | Fig. 3 | PASS |
| P1-010 | Abstract 8 componentes na ordem | anotado no fonte | PASS |
| P1-011 | Baseline principal 7 etapas | Groth16: Table I destacado, §II.A, §VI baseline subsection, Intro, Figs 4-6 | PASS |
| P1-012 | Related work: 1 parágrafo por trabalho | §II | PASS |
| P1-013 | Table II Experimental Setup completa | §VI, table*, categorias presentes; AI Models omitido com justificativa (regra: remover N/A) | PASS |
| P1-014 | 3 agentes com métricas individuais | PA/VA/RA + Table IV | PASS |
| P1-015 | Testes estatísticos (t-test) | §VI.F, statistical_tests.json | PASS |
| P1-016 | Ablation study | §VI.G | PASS |
| P1-017 | Acknowledgment Bloco 1 literal | comparação literal | PASS |
| P1-018 | Acknowledgment Bloco 2 literal | substituído pelo texto literal (ciclo 01) | PASS |
| P1-019 | Author Information + ORCID 0000-0002-7068-8889 | IEEEbiography | PASS |
| P1-020 | Estrutura de repositório (README, paper/, src/, data/, notebooks/, scripts/, LICENSE) | src/ e notebooks/ populados (ciclo 01); figures/ documentado (TikZ inline) | PASS |
| P1-021 | Segurança A100 / .gitignore obrigatório | scan + git ls-files | PASS |
| P1-022 | Compilação tectonic | PASS, 0 erros | PASS |
| P1-023 | Security Analysis and Compliance section | §V | PASS |
| P1-024 | GitHub não vazio ao ser citado | ufxa/zkauth populado | PASS |
