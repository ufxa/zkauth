# Ciclo 00 — Full Review (painel: EIC + Metodologia + Domínio + Perspectiva + Devil's Advocate)

Skill: academic-paper-reviewer (modo full, read-only). Manuscrito: paper/main.tex @ e4e1197.
Este manuscrito já havia passado por 2 rodadas completas (v2-v4, decisões MAJOR→MINOR);
os achados abaixo são os remanescentes encontrados nesta rodada, com foco adversarial
em rastreabilidade de dados (Devil's Advocate + Auditor de Evidências da Fase 2).

## Achados CRITICAL

- **C-001 (Devil's Advocate / Evidence Auditor)** — Valores plotados nas Figuras 4, 5 e 6
  não correspondem aos arquivos de resultado `data/results/*.csv` citados como fonte.
  Evidência: Fig. 5 mostrava Groth16 Replay = 3.8%, CSV registra 2.64%; Fig. 6 mostrava
  ZK-STARK 44.7→57.7 ms (+29%), mas o modelo O(log n) da simulação produz ≈+98%;
  os error bars da Fig. 6 não tinham coluna de variância correspondente no CSV
  (IC "calibrado", não medido). Viola integridade de resultados (Fase 2 §B) e
  P1-008.

## Achados MAJOR

- **M-001 (IEEE Auditor)** — Acknowledgment Bloco 2 não é literal ao bloco fixo da
  Fase 1 (texto reescrito em outra redação; instituições LaCIS/UFPA e menções a
  Governo do Pará/Federal ausentes). Viola P1-018 ("não modificar").
- **M-002 (Evidence Auditor)** — `src/` e `notebooks/` vazios no repositório público
  citado como evidência de reprodutibilidade (Fase 1 estrutura obrigatória; Fase 2
  §D "código citado no artigo realmente existe").
- **M-003 (IEEE Auditor)** — Travessões/duplos hífens em prosa (linhas 190-191, 1394,
  1457-1459), proibidos pela Fase 1.

## Achados MINOR (registrados, não bloqueiam)

- m-001 — 41% das referências são pré-2023 (limite preferencial: 20%). Justificável
  por primitivas fundacionais de criptografia; registrado como desvio documentado.
- m-002 — 2 referências (looker2023bbs, w3c_sdjwt_2024) sem DOI; são standards
  W3C/IETF com identificadores formais próprios (CR/draft numbers) — prática aceita.
- m-003 — Overfull hbox ≤ 5.5pt em 3 parágrafos (cosmético).

## Decisão editorial do ciclo 00: MAJOR REVISION (C-001 impede aceitação)
