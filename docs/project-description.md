# Project Description

## Chosen Project

The chosen project is Keras (Keras 3), a high-level deep learning framework maintained by the keras-team.

## What This Recovery Project Does

This repository documents a software architecture recovery study of Keras. The work is organized week by week and combines reading notes, diagrams, experiments, and interpretation artifacts.

## Scope of Recovery

The recovery scope focuses on three architecture views:
- Module view (static code-level structure)
- C&C view (runtime interactions)
- Allocation view (mapping to backend runtimes and hardware)

## Why Keras Was Selected

Keras is a strong architecture-recovery target because it is:
- Mature and widely used
- Multi-backend by design (TensorFlow, JAX, PyTorch)
- Rich in architectural patterns and abstraction boundaries
- Practical for studying quality attributes such as modifiability and portability
