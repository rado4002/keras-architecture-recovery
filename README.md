# Keras Architecture Recovery

This repository contains a week-by-week software architecture recovery study of Keras (Keras 3), built as a solo course project.

The project goal is to recover and document how Keras is structured, how it behaves at runtime, and how its design supports quality attributes such as modifiability, portability, and maintainability.

## Project Objectives

- Recover architecture using multiple complementary views:
	- Module view (static structure)
	- C&C view (runtime behavior)
	- Allocation view (software to runtime/hardware mapping)
- Validate architectural claims with small runnable experiments
- Produce reusable documentation artifacts each week
- Build a cumulative interpretation of Keras design patterns and responsibilities

## Core Project Topics (Separate Files)

The required project topics are documented as separate files:

- Project description: `docs/project-description.md`
- Business context: `docs/business-context.md`
- Key quality concerns: `docs/key-quality-concerns.md`
- Early architecture design decisions (recovered): `docs/early-architecture-design-decisions-recovered.md`

## Repository Structure

```text
keras-architecture-recovery/
├── README.md
├── docs/
│   ├── architecture-recovery-process.md
│   ├── business-context.md
│   ├── early-architecture-design-decisions-recovered.md
│   ├── key-quality-concerns.md
│   ├── project-description.md
│   └── reusable-project-framework.md
├── vendor/
│   └── keras/                 # local vendor snapshot/reference
└── weeks/
		├── week01/
		├── week02/
		├── week03/
		└── week04/
```

## Weekly Workflow

Each week follows the same structure:

- `docs/`: reading notes and theory mapping
- `diagrams/`: architecture diagrams with interpretation
- `experiments/`: minimal evidence scripts
- `interpretation/`: synthesized responsibilities, patterns, and findings
- `README.md`: week-level summary and artifact index

## Week Index

### Week 01

- Focus: foundational reconnaissance and first architecture mapping
- Main outputs:
	- `weeks/week01/README.md`
	- `weeks/week01/docs/Reading Note1.md`
	- `weeks/week01/diagrams/README.md`

### Week 02

- Focus: dependency discovery, forward/backward flow, allocation basics
- Main outputs:
	- `weeks/week02/README.md`
	- `weeks/week02/docs/Reading Note2.md`
	- `weeks/week02/diagrams/README.md`
	- `weeks/week02/experiments/README.md`

### Week 03

- Focus: C&C runtime sequence and component-level interpretation
- Main outputs:
	- `weeks/week03/README.md`
	- `weeks/week03/docs/Reading Note3.md`
	- `weeks/week03/diagrams/README.md`
	- `weeks/week03/experiments/README.md`
	- `weeks/week03/interpretation/Responsibilities, Patterns, and Findings.md`

### Week 04

- Focus: multi-view documentation quality and modifiability analysis
- Main outputs:
	- `weeks/week04/README.md`
	- `weeks/week04/docs/Reading Note4.md`
	- `weeks/week04/diagrams/README.md`
	- `weeks/week04/experiments/README.md`
	- `weeks/week04/interpretation/Responsibilities, Patterns, and Findings.md`

## How to Run Experiments

From repository root:

```powershell
& .\.venv\Scripts\Activate.ps1
```

Then run a week-specific experiment, for example:

```powershell
python "weeks/week04/experiments/experiments1-backend switching"
```

Note:
- Some experiment files are executable Python scripts without a `.py` extension.

## Method Summary

The recovery process used in this project combines:

1. Reading and theory extraction (architecture concepts)
2. Static code and dependency observation
3. Runtime tracing through small experiments
4. Diagram construction (Module/C&C/Allocation)
5. Pattern and responsibility interpretation

For process details, see:
- `docs/architecture-recovery-process.md`
- `docs/reusable-project-framework.md`

For core project topic statements, see:
- `docs/project-description.md`
- `docs/business-context.md`
- `docs/key-quality-concerns.md`
- `docs/early-architecture-design-decisions-recovered.md`

## Current Status

- Weeks 01-04 contain documented artifacts across docs, diagrams, and weekly summaries.
- Week 04 structure has been aligned with the same format used in previous weeks.
- The project is ready to continue with Week 05 using the same workflow template.

## License and Source Note

- Keras source is included under `vendor/keras/` for architecture study context.
- Refer to `vendor/keras/LICENSE` for upstream licensing terms.
