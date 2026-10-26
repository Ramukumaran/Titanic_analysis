# Titanic Data Analysis

A Python-based exploratory data analysis (EDA) project that examines Titanic passenger data using **Pandas, NumPy, Matplotlib, and Seaborn**. The project demonstrates data inspection, data cleaning, descriptive analysis, and visualization in a practical workflow.

## Overview

The goal of this project is to explore passenger characteristics and survival patterns in the Titanic dataset. It is designed as a learning project for practicing core data analysis techniques with Python.

## Objectives

- Load and inspect a CSV dataset using Pandas.
- Identify and handle missing values and duplicate records.
- Summarize passenger survival, gender, age, class, and fare information.
- Apply basic numerical operations with NumPy.
- Create visualizations to communicate patterns in the data.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, grouping, and analysis |
| NumPy | Numerical operations and summary calculations |
| Matplotlib | Chart creation |
| Seaborn | Statistical visualizations |

## Project Structure

```text
titanic-data-analysis/
├── titanic_analysis.py
├── titanic_data.csv
├── graph1_bar_survival.png
├── graph2_pie_gender.png
├── graph3_hist_age.png
├── graph4_line_fare.png
├── graph5_seaborn_survival_gender.png
├── graph6_seaborn_boxplot.png
├── graph7_seaborn_heatmap.png
├── graph8_seaborn_fare_class.png
├── .gitignore
└── README.md
```

*Note: The chart images are generated when the script runs. Keep the CSV dataset in the same directory as the Python script.*

## Analysis and Visualizations

The script produces the following charts:

1. **Survival Count** — compares passengers who survived with those who did not.
2. **Gender Distribution** — shows the distribution of passengers by gender.
3. **Age Distribution** — displays the distribution of passenger ages.
4. **Fare by Passenger ID** — plots fares for the first 100 passengers.
5. **Survival by Gender** — compares survival counts across genders.
6. **Age by Passenger Class** — compares age distributions across passenger classes.
7. **Correlation Heatmap** — visualizes correlations among selected numeric columns.
8. **Average Fare by Passenger Class** — compares average fares across passenger classes.

## Getting Started

### Prerequisites

- Python 3.9 or later recommended
- `pip`

### 1. Get the project

If the project is hosted on GitHub, clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Alternatively, download and extract the project ZIP.

### 2. Create a virtual environment (recommended)

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If you use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install numpy pandas matplotlib seaborn
```

### 4. Run the analysis

Ensure `titanic_analysis.py` and `titanic_data.csv` are in the same folder, then run:

```bash
python titanic_analysis.py
```

The script prints analysis results in the terminal, displays plots, and saves chart images to the current working directory. If plots appear in separate windows, close each window to continue.

## Dataset

The project uses `titanic_data.csv`. Relevant columns include:

| Column | Description |
|---|---|
| `Survived` | Survival indicator: `0` = did not survive, `1` = survived |
| `Pclass` | Passenger class |
| `Sex` | Passenger gender |
| `Age` | Passenger age |
| `SibSp` | Number of siblings/spouses aboard |
| `Parch` | Number of parents/children aboard |
| `Fare` | Passenger fare |
| `Embarked` | Port of embarkation |

## Data Cleaning

The script demonstrates several common preprocessing operations:

- Checking missing values.
- Filling missing `Age` values with the mean.
- Filling missing `Embarked` values with the mode.
- Dropping the `Cabin` column due to extensive missing data.
- Removing duplicate rows and resetting the index.

These transformations are performed in memory; the original CSV file is not overwritten.

## Key Takeaways

This project provides hands-on practice with:

- Reading and inspecting structured data.
- Cleaning missing and duplicate data.
- Filtering, grouping, sorting, and summarizing records.
- Calculating descriptive statistics.
- Building charts to communicate findings.
- Organizing a Python analysis project for version control and GitHub.

## Limitations

- This is an exploratory data analysis project; it does not train a predictive machine-learning model.
- Mean imputation for age is used as a simple demonstration and may not be the best method for every analysis.
- The `Cabin` column is excluded from the analysis because it contains many missing values.

## Author

**Kumaran R**

---

*This project was created for learning and demonstrating foundational Python data analysis skills.*
