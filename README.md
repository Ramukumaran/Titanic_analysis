# Titanic Data Analysis with Python

A beginner-friendly data analysis project that explores the Titanic passenger dataset using **NumPy, Pandas, Matplotlib, and Seaborn**. The script demonstrates basic Python data analysis, data cleaning, descriptive statistics, and data visualization.

## Project Overview

This project analyzes passenger information from the Titanic dataset to explore survival counts, passenger demographics, age distribution, fares, and relationships between selected numerical variables.

## Features

- **NumPy basics:** calculate mean, minimum, maximum, sum, and sort an array.
- **Explore data with Pandas:** view rows, dataset dimensions, column names, summary statistics, and data types.
- **Clean the data:** inspect missing values, fill missing ages with the mean, fill missing embarkation ports with the mode, drop the `Cabin` column, remove duplicate rows, and reset the index.
- **Analyze data:** count survivors, inspect passenger classes and gender counts, group passengers by gender, and sort passengers by age.
- **Visualize data:** generate eight charts using Matplotlib and Seaborn.

## Technologies Used

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn

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

The graph image files are created when the script runs. Keep `titanic_data.csv` in the same folder as `titanic_analysis.py`.

## Visualizations

The script creates these charts:

1. **Survival count** — number of passengers who survived and did not survive.
2. **Gender distribution** — proportion of male and female passengers.
3. **Age distribution** — histogram of passenger ages.
4. **Fare by passenger ID** — fares for the first 100 passengers.
5. **Survival by gender** — survival counts grouped by gender.
6. **Age by passenger class** — box plot of age distributions for each class.
7. **Correlation heatmap** — correlations between survival, passenger class, age, and fare.
8. **Average fare by passenger class** — average fare for each passenger class.

## Getting Started

### 1. Install Python

Install Python 3 from [python.org](https://www.python.org/downloads/) if it is not already installed.

### 2. Download or clone the repository

If the project is on GitHub, clone it using:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Alternatively, download the repository ZIP and extract it.

### 3. (Optional) Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the script using the virtual environment's Python directly, or use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install the required libraries

```bash
python -m pip install numpy pandas matplotlib seaborn
```

### 5. Run the analysis

Make sure `titanic_analysis.py` and `titanic_data.csv` are in the same directory, then run:

```bash
python titanic_analysis.py
```

The script prints analysis results in the terminal, displays charts, and saves the eight chart images in the project folder. Close each chart window to continue if your Python environment displays plots one at a time.

## Dataset

The file `titanic_data.csv` contains passenger information such as:

- `Survived` — `0` means did not survive; `1` means survived.
- `Pclass` — passenger class.
- `Sex` and `Age` — passenger demographics.
- `SibSp` and `Parch` — family relationships aboard.
- `Fare` — fare paid.
- `Embarked` — port of embarkation.

The script makes cleaning changes in memory; it does **not** overwrite the original CSV file.

## Key Learning Outcomes

By working through this project, you can practice:

- Loading and inspecting CSV data.
- Handling missing values and duplicate rows.
- Using filtering, grouping, sorting, and concatenation in Pandas.
- Calculating descriptive statistics with NumPy and Pandas.
- Creating charts and a correlation heatmap.
- Organizing a small Python data analysis project for GitHub.

## Notes and Limitations

- This is an exploratory data analysis project, not a machine-learning model.
- Filling missing ages with the mean is a simple learning example; other approaches may be more appropriate for deeper analysis.
- The `Cabin` column is dropped because it contains many missing values.
- The charts are saved in the current working directory when the script is run.

## Author

**Kumaran R**

---

If you find this project useful for learning Python data analysis, feel free to star the repository.
