# Reusable Framework: Architecture Recovery Project Design

Use this as a copy-ready blueprint for any software architecture recovery project.

## 1) Core Design Principles

- Organize by **time-boxed iteration** (week/sprint), not by artifact type only.
- Keep one **stable root methodology** document for consistency.
- Keep each iteration self-contained with evidence, diagrams, interpretation, and outputs.
- Prefer formats that render natively on GitHub (Markdown + Mermaid).
- Use naming conventions that scale (`week01`, `week02`, ...).

## 2) Scalable Folder Blueprint

```text
project-root/
├── docs/
│   └── architecture-recovery-process.md
├── weeks/
│   ├── week01/
│   │   ├── docs/
│   │   ├── diagrams/
│   │   ├── experiments/
│   │   ├── interpretation/
│   │   ├── notes/
│   │   ├── qa/
│   │   └── slides/
│   ├── week02/ (same structure)
│   └── week03/ (same structure)
└── vendor/ (optional: source under study)
```

## 3) Why This Structure Works

- **Clarity**: each week tells a complete story from evidence to conclusions.
- **Scalability**: adding a new week is predictable and low-friction.
- **Traceability**: every claim can be mapped to experiment, diagram, and interpretation.
- **Reusability**: same structure applies to any framework/system (not just Keras).

## 4) Weekly Execution Framework

For each `weekXX`, run this cycle:

1. **Plan**
   - Define 2–4 focused architecture questions.
2. **Experiment**
   - Run minimal scripts to produce evidence.
3. **Recover Views**
   - Update Module, C&C, and Allocation understanding.
4. **Interpret**
   - Write subsystem responsibilities and pattern findings.
5. **Review**
   - Check consistency between diagrams, logs, and findings.
6. **Publish**
   - Commit, push, and summarize week outputs.

## 5) Standard Artifacts Per Week

- `README.md`
  - objectives, methods, experiments, findings, blockers, next week plan.
- `docs/*`
   - reading notes and supplementary weekly documents.
- `diagrams/*.md`
  - Mermaid diagrams with concise titles and legend/notes.
- `experiments/*`
  - runnable scripts with clear filenames and focused purpose.
- `interpretation/*`
  - architecture views summary, responsibilities, patterns.
- `qa/*`
  - validation questions and answers for architectural claims.

## 6) Quality Gates (Definition of Done)

A week is done when all are true:

- At least one updated diagram is viewable on GitHub.
- At least one experiment supports each major claim.
- `README.md` includes blockers + next steps.
- Terminology is consistent across docs/diagrams.
- All files follow naming conventions (no spaces/special chars).

## 7) Naming Rules

- Week folders: `week01`, `week02`, `week03`, ...
- Weekly logs: `weeks/weekXX/README.md`
- Diagrams: `module-view.md`, `module-decomposition.md`, `c-and-c-view.md`, `allocation-view.md`
- Experiments: `exp01_<purpose>.py`, `exp02_<purpose>.py`

## 8) Fast Start for New Projects

1. Copy this folder blueprint.
2. Create `docs/architecture-recovery-process.md`.
3. Create `weeks/week01/...` subfolders.
4. Add placeholders (`.gitkeep`) in empty folders.
5. Start with one focused architecture question and one experiment.

## 9) Minimal Weekly Checklist Template

```markdown
# Week XX Log

## Objectives
- 

## Experiments
- 

## Architecture Findings
- Module View:
- C&C View:
- Allocation View:

## Evidence Links
- 

## Blockers
- 

## Next Week Plan
- 
```

## 10) Adaptation Guide (Use in Other Domains)

- Replace `vendor/` with the system under study.
- Keep `weeks/` unchanged to preserve cadence and comparability.
- Rename only domain terms in docs (not structural folders).
- Add domain-specific artifacts only when needed (e.g., `benchmarks/`).

---

If reused in another repository, keep this file as `docs/reusable-project-framework.md` and adjust only domain-specific wording.
