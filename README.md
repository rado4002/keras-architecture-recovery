# ⭐ Recovering the Architecture of Keras  

## 📌 Project Context  

This repository contains a **solo academic software architecture recovery project** focused on analyzing and documenting the architecture of the open-source deep learning framework **Keras**.

The project is conducted as part of an introductory course in **Software Architecture**.

## 🤖 What is Keras?

**Keras** is a high-level deep learning framework for building and training neural networks in Python.

In practical terms, Keras lets you define models with clean APIs (`Sequential`, Functional API, or subclassing) while delegating heavy numerical computation to backend engines.

Modern Keras (Keras 3) is designed for **multi-backend execution**, allowing workflows across engines such as TensorFlow, JAX, and PyTorch through a unified developer experience.

This makes Keras a strong case study for architecture recovery because it combines:

- clean API-layer design
- modular subsystem organization
- runtime orchestration logic
- backend and hardware abstraction



The work combines:

- theoretical architecture concepts  
- reverse-engineering techniques  
- controlled experimentation  
- progressive technical documentation  

---

## 🎯 Project Objectives  

The primary objective is to **recover and understand the architectural structure of Keras** from both static and dynamic perspectives.

Key goals include:

- Recover the **Module View**  
  → Understand logical organization and subsystem responsibilities  

- Recover the **Component-and-Connector (C&C) View**  
  → Analyze runtime execution flow of model training and inference  

- Recover the **Allocation View**  
  → Study how computation maps to execution environments (CPU / backend engines)

- Identify **architectural patterns** used in the framework  

- Develop a **fundamental conceptual understanding of AI model pipelines**

- Apply software architecture theory to a **large-scale industrial framework**

---

## 🧠 Learning Philosophy  

This project follows a **Learning-by-Doing Architecture Recovery Approach**.

Instead of only reading documentation, each learning cycle includes:

- Executing small controlled Keras experiments  
- Observing system structure and runtime behavior  
- Building architectural diagrams  
- Writing responsibility-driven interpretations  
- Refining mental models progressively  

The objective is to develop:

- architectural observation skills  
- system reasoning capability  
- technical documentation discipline  


## 🏗️ Project Structure
```
keras-architecture-recovery/
│
├── docs/
│   └── architecture-recovery-process.md → Shared methodology
├── weeks/
│   ├── week01/
│   │   ├── README.md → Weekly log and summary
│   │   ├── docs/ → Reading notes and supplementary docs
│   │   ├── diagrams/ → Mermaid architecture diagrams
│   │   ├── experiments/ → Runnable exploration scripts
│   │   ├── interpretation/ → Architectural analysis and findings
│   │   ├── qa/ → Weekly QA exercises
│   │   └── slides/ → Weekly presentation assets
│   ├── week02/ (same structure)
│   └── week03/ (same structure)
└── vendor/ → Vendored Keras source used for recovery

```


Each **weekly folder** contains:

- week-level README log  
- experiments  
- diagrams  
- interpretation files  
- docs (reading notes + supporting notes)  

This incremental structure ensures continuous project maturity.

---

## 🔬 Methodology  

Architecture recovery is conducted using a **systematic engineering approach**:

### 1️⃣ Static Analysis  
- Source code module exploration  
- Dependency observation  
- subsystem identification  

### 2️⃣ Dynamic Analysis  
- Forward execution tracing  
- training loop experimentation  
- backend delegation observation  

### 3️⃣ Architectural Synthesis  
- Construction of architecture views  
- identification of design patterns  
- responsibility interpretation  

### 4️⃣ Iterative Refinement  
- Weekly documentation updates  
- diagram improvement  
- conceptual clarification  

---

## 📊 Architecture Views Targeted  

The project aims to progressively reconstruct:

- **Module View** → subsystem decomposition and dependency structure  
- **Component & Connector View** → runtime computational pipeline  
- **Allocation View** → mapping between framework logic and hardware/backend execution  

These views follow **standard software architecture documentation practices.**

---

## 🚀 Expected Learning Outcomes  

By the end of the project, the following outcomes are expected:

- Ability to analyze architecture of complex open-source systems  
- Practical understanding of deep learning execution pipelines  
- Experience in architecture recovery techniques  
- Identification of modern framework architectural patterns  
- Creation of a professional technical portfolio artifact  

---

## 📅 Current Project Status  

✅ **Week 01 Completed — Initial Architecture Reconnaissance**

- Environment and repository setup completed
- Core Keras module mapping completed (models, layers, ops, backend abstraction)
- Initial forward-pass runtime tracing completed
- First architecture patterns identified (layered + pipeline)
- Initial responsibility analysis documented

✅ **Week 02 Completed — Module, C&C, and Allocation Deepening**

- Static dependency discovery validated (`layers → ops → backend`)
- Forward-pass flow traced with custom debug layer instrumentation
- Backward/gradient flow recovered with manual training-step experiment
- Device allocation view documented (Python orchestration vs backend/hardware execution)
- Architectural interpretation finalized (modularity, delegation, pattern analysis)

🟡 **Week 03 In Progress — Next Recovery Phase**

Current focus:

- Expand C&C analysis for Functional API and multi-layer model structures
- Trace full `model.fit()` runtime call chain across backends
- Refine inter-layer dependency and optimization pattern documentation

---

## 📖 Motivation  

Modern software engineers increasingly interact with **AI-driven platforms and computational frameworks**.

Understanding their architecture provides:

- stronger system design intuition  
- better debugging and optimization capability  
- improved ability to integrate AI into large software systems  

Keras is selected as the study subject because it represents:

- a real industrial-grade AI framework  
- a modular layered architecture  
- a system combining APIs, mathematical engines, and hardware abstraction  

This project aims to bridge the gap between  
**classical software architecture education**  
and  
**modern intelligent software systems.**

