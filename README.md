# 1D Heat Conduction Solver Using FiPy

Finite Volume Method (FVM) implementation of the one-dimensional heat conduction equation using FiPy.

## Features

* Steady-state heat conduction
* Transient heat conduction
* Dirichlet boundary conditions
* Neumann boundary conditions
* Robin boundary conditions
* Source and no-source formulations
* Mesh convergence study
* Time-step convergence study
* Numerical vs analytical validation
* Error analysis

## Overview

This repository presents the numerical solution of the one-dimensional heat conduction equation using the Finite Volume Method (FVM) implemented in FiPy.

The project investigates transient and steady-state heat transfer under different boundary conditions and compares numerical results with analytical solutions.

The work was carried out as part of an M.Tech study in computational welding, heat transfer modeling, and numerical methods.

## Governing Equation

### Steady-State Heat Equation

d²T/dx² = 0

### Transient Heat Equation

∂T/∂t = α ∂²T/∂x² + S

where:

* T = Temperature
* α = Thermal Diffusivity
* S = Internal Heat Source

## Objectives

* Solve the 1D heat equation using FiPy.
* Study Dirichlet, Neumann, and Robin boundary conditions.
* Investigate transient and steady-state heat transfer.
* Validate numerical solutions against analytical solutions.
* Perform mesh convergence and timestep convergence studies.
* Quantify numerical error and solution accuracy.

## Cases Studied

### Case 1: Dirichlet Boundary Condition (No Source)

Fixed temperatures at both boundaries.

### Case 2: Dirichlet Boundary Condition (With Source)

Uniform heat generation inside the domain.

### Case 3: Neumann Boundary Condition (No Source)

Specified heat flux at the boundary.

### Case 4: Neumann Boundary Condition (With Source)

Heat flux boundary condition with internal heat generation.

### Case 5: Robin Boundary Condition (No Source)

Convective heat transfer at the boundary.

### Case 6: Robin Boundary Condition (With Source)

Convective boundary condition with heat generation.

## Numerical Method

The governing heat equation is solved using the Finite Volume Method (FVM) available in the FiPy PDE solver framework.

Simulations include:

* Transient evolution
* Steady-state solution
* Mesh independence study
* Time-step independence study
* Numerical–analytical comparison
* Error analysis

## Software Environment

* Python 3.14
* FiPy 4.0.2
* NumPy
* Matplotlib

## Repository Structure

1D-Heat-Conduction-FiPy

│

├── Case_1_Dirichlet_NoSource

├── Case_2_Dirichlet_Source

├── Case_3_Neumann_NoSource

├── Case_4_Neumann_Source

├── Case_5_Robin_NoSource

├── Case_6_Robin_Source

├── Figures

└── README.md

## Key Results

* Numerical solutions agree closely with analytical solutions.
* Mesh convergence studies confirm grid-independent solutions.
* Time-step convergence studies verify numerical stability.
* Error analysis demonstrates high numerical accuracy.
* Boundary conditions were successfully implemented and validated.

## Future Work

* 2D Heat Conduction
* 3D Heat Conduction
* Moving Heat Source
* Rosenthal Welding Model
* Goldak Double Ellipsoidal Heat Source
* Welding Thermal Cycle Analysis
* Welding Temperature Distribution
* Heat Affected Zone (HAZ) Prediction

## Author

Sonali Savane

M.Tech Project Work

Computational Welding and Heat Transfer Modeling

