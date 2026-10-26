# ============================================================
#   TITANIC DATA ANALYSIS - Beginner Friendly
#   Libraries Used: NumPy, Pandas, Matplotlib, Seaborn
# ============================================================
# NOTE: Keep "titanic_data.csv" in the same folder as this file


# ──────────────────────────────────────────────
# STEP 1: IMPORT LIBRARIES
# ──────────────────────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ──────────────────────────────────────────────
# STEP 2: NUMPY BASICS
# ──────────────────────────────────────────────
print("=" * 40)
print("NUMPY BASICS")
print("=" * 40)

arr = np.array([22, 38, 26, 35, 28, 45, 30, 19])  # sample ages

print("Array         :", arr)
print("Mean (Average):", np.mean(arr))
print("Max Value     :", np.max(arr))
print("Min Value     :", np.min(arr))
print("Sum           :", np.sum(arr))
print("Sorted Array  :", np.sort(arr))


# ──────────────────────────────────────────────
# STEP 3: LOAD DATA WITH PANDAS
# ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("PANDAS BASICS")
print("=" * 40)

df = pd.read_csv("titanic_data.csv")          # load the CSV file

print("\n-- First 5 Rows (head) --")
print(df.head())

print("\n-- Last 5 Rows (tail) --")
print(df.tail())

print("\n-- Dataset Shape (rows, columns) --")
print(df.shape)

print("\n-- Column Names --")
print(df.columns.tolist())

print("\n-- Basic Statistics --")
print(df.describe())

print("\n-- Data Types --")
print(df.dtypes)


# ──────────────────────────────────────────────
# STEP 4: DATA PREPROCESSING
# ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("DATA PREPROCESSING")
print("=" * 40)

# 4a. Check missing values
print("\n-- Missing Values --")
print(df.isnull().sum())

# 4b. Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 4c. Fill missing Embarked with most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 4d. Drop Cabin column (too many missing values)
df = df.drop(columns=["Cabin"])

# 4e. Remove duplicate rows
df = df.drop_duplicates()

# 4f. Reset index after cleaning
df = df.reset_index(drop=True)

print("\n-- Missing Values After Cleaning --")
print(df.isnull().sum())

print("\n-- New Shape After Cleaning --")
print(df.shape)


# ──────────────────────────────────────────────
# STEP 5: PANDAS EXTRA COMMANDS
# ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("MORE PANDAS COMMANDS")
print("=" * 40)

# Select one column
print("\n-- Age Column (first 5) --")
print(df["Age"].head())

# Filter rows: only survivors
survivors = df[df["Survived"] == 1]
print("\n-- Total Survivors --", len(survivors))

# Value counts
print("\n-- Passenger Class Count --")
print(df["Pclass"].value_counts())

print("\n-- Gender Count --")
print(df["Sex"].value_counts())

# Group by
print("\n-- Average Age by Gender --")
print(df.groupby("Sex")["Age"].mean())

# Concat example: split and rejoin
df_part1 = df[:400]
df_part2 = df[400:]
df_combined = pd.concat([df_part1, df_part2])
print("\n-- After Concat, Total Rows --", len(df_combined))

# Rename a column
df = df.rename(columns={"SibSp": "Siblings_Spouses"})
print("\n-- Column renamed: SibSp → Siblings_Spouses")

# Sort by Age
print("\n-- Top 5 Oldest Passengers --")
print(df.sort_values("Age", ascending=False)[["Name", "Age"]].head())


# ──────────────────────────────────────────────
# STEP 6: MATPLOTLIB GRAPHS
# ──────────────────────────────────────────────

# --- Graph 1: Bar Chart - Survival Count ---
plt.figure(figsize=(6, 4))
df["Survived"].value_counts().plot(kind="bar", color=["red", "green"])
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("graph1_bar_survival.png")
plt.show()

# --- Graph 2: Pie Chart - Gender Split ---
plt.figure(figsize=(5, 5))
df["Sex"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["skyblue", "pink"])
plt.title("Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("graph2_pie_gender.png")
plt.show()

# --- Graph 3: Histogram - Age Distribution ---
plt.figure(figsize=(6, 4))
plt.hist(df["Age"], bins=20, color="steelblue", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("graph3_hist_age.png")
plt.show()

# --- Graph 4: Line Chart - Fare over Passenger ID ---
plt.figure(figsize=(7, 4))
plt.plot(df["PassengerId"][:100], df["Fare"][:100], color="orange")
plt.title("Fare Paid (First 100 Passengers)")
plt.xlabel("Passenger ID")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("graph4_line_fare.png")
plt.show()


# ──────────────────────────────────────────────
# STEP 7: SEABORN GRAPHS
# ──────────────────────────────────────────────

# --- Graph 5: Count Plot - Survival by Gender ---
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex", hue="Survived", palette="Set2")
plt.title("Survival Count by Gender")
plt.tight_layout()
plt.savefig("graph5_seaborn_survival_gender.png")
plt.show()

# --- Graph 6: Box Plot - Age by Class ---
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Pclass", y="Age", palette="pastel")
plt.title("Age Distribution by Passenger Class")
plt.tight_layout()
plt.savefig("graph6_seaborn_boxplot.png")
plt.show()

# --- Graph 7: Heatmap - Correlation ---
plt.figure(figsize=(7, 5))
sns.heatmap(df[["Survived", "Pclass", "Age", "Fare"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("graph7_seaborn_heatmap.png")
plt.show()

# --- Graph 8: Bar Plot - Avg Fare by Class ---
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="Pclass", y="Fare", palette="Blues")
plt.title("Average Fare by Passenger Class")
plt.tight_layout()
plt.savefig("graph8_seaborn_fare_class.png")
plt.show()


# ──────────────────────────────────────────────
# DONE!
# ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("Analysis Complete! All graphs saved.")
print("=" * 40)
