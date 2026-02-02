# MATH60082 Python Support Labs

Notebooks and supporting materials for the MATH60082 Python support labs and related lectures.

## Quick start
- Install Anaconda (see `MATH60082-installing-anaconda.ipynb`).
- Create the course environment: `conda env create -f environment.yml`.
- Open notebooks or run scripts in VS Code (see the running guides below).

## Repository layout
- `environment.yml` - conda environment definition used in the course.
- `examples/` - small support-class Python scripts (with some solutions).
- `solutions/` - solution notebooks for coding workbooks and lab classes.
- `images/` - figures used in the notebooks.

## Notebooks

### Setup and tooling
- `MATH60082-installing-anaconda.ipynb` - Installing Anaconda on Windows (with a macOS note).
- `MATH60082-running-notebooks.ipynb` - Running Jupyter notebooks in VS Code inside Anaconda.
- `MATH60082-running-vscode.ipynb` - Running Python files in VS Code inside Anaconda.

### Coding support classes
- `MATH60082-coding-support-class-1.ipynb` - What a program is, why Python, basic syntax and types.
- `MATH60082-coding-support-class-2.ipynb` - Control flow (if statements, loops) plus practice tasks.

### Coding workbooks
- `MATH60082-coding-workbook-1.ipynb` - Practice tasks to accompany Coding Support Class 1.
- `MATH60082-coding-workbook-2.ipynb` - Practice tasks to accompany Coding Support Class 2.

### Lab classes and workbooks (Weeks 2-10)
The lab class notebooks introduce concepts and demos; the matching lab workbook is a task sheet for practice.

| Week | Lab class notebook | Lab workbook notebook | Focus |
| --- | --- | --- | --- |
| 2 | `MATH60082-lab-class-2.ipynb` | `MATH60082-lab-workbook-2.ipynb` | Solving problems with computers; knock-out barrier option demo; benchmarking |
| 3 | `MATH60082-lab-class-3.ipynb` | `MATH60082-lab-workbook-3.ipynb` | ODEs; Euler method; consistency and convergence |
| 4 | `MATH60082-lab-class-4.ipynb` | `MATH60082-lab-workbook-4.ipynb` | Random numbers; distributions; rolling the dice |
| 5 | `MATH60082-lab-class-5.ipynb` | `MATH60082-lab-workbook-5.ipynb` | Law of large numbers; Monte Carlo for European calls; central limit theorem |
| 6 | `MATH60082-lab-class-6.ipynb` | `MATH60082-lab-workbook-6.ipynb` | Stochastic volatility; path dependent options |
| 7 | `MATH60082-lab-class-7.ipynb` | `MATH60082-lab-workbook-7.ipynb` | Binomial trees; evaluating convergence |
| 8 | `MATH60082-lab-class-8.ipynb` | `MATH60082-lab-workbook-8.ipynb` | Finite difference approximations; boundary conditions; stability and efficiency |
| 9 | `MATH60082-lab-class-9.ipynb` | `MATH60082-lab-workbook-9.ipynb` | Crank-Nicolson method; matrix form; stability and convergence |
| 10 | `MATH60082-lab-class-10.ipynb` | `MATH60082-lab-workbook-10.ipynb` | American options; penalty method |

### Lecture supplements
- `MATH60082-lecture-LeastSquares.ipynb` - Lecture 9: Least Squares Monte Carlo (Longstaff and Schwartz).
- `MATH60082-lecture-Quadrature.ipynb` - Lecture 10: Quadrature (call option and barrier option examples).
