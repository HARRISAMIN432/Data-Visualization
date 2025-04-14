import matplotlib.pyplot as plt
import seaborn as sns
from Dataset import df
    

def plot_alcohol_vs_heart_rate():
    plt.figure(figsize=(8,5))
    sns.barplot(x="Alcohol_Consumption_per_Week", y="Heart_Rate", data=df, palette="Blues_d")
    plt.title("Alcohol Consumption vs Heart Rate")
    plt.xlabel("Alcohol Consumption (per Week)")
    plt.ylabel("Heart Rate")
    plt.show()


def plot_bmi_vs_age():
    plt.figure(figsize=(8,5))
    sns.regplot(x="Age", y="BMI", data=df, scatter_kws={'s': 100, 'alpha': 0.5}, line_kws={'color': 'red'})
    plt.title("BMI vs Age with Regression Line")
    plt.xlabel("Age")
    plt.ylabel("BMI")
    plt.show()


def plot_facetgrid_steps_vs_bmi():
    g = sns.FacetGrid(df, col="Gender", height=5, aspect=1.2)
    g.map(sns.scatterplot, "Daily_Steps", "BMI", alpha=0.7)
    g.set_axis_labels("Daily Steps", "BMI")
    g.set_titles("{col_name} Gender")
    g.fig.suptitle("Daily Steps vs BMI by Gender", y=1.05)
    plt.show()


def plot_age_distribution():
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=20, kde=True)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

def plot_bmi_distribution():
    plt.figure(figsize=(8,5))
    sns.histplot(df['BMI'], bins=20, kde=True, color="green")
    plt.title("BMI Distribution")
    plt.xlabel("BMI")
    plt.ylabel("Count")
    plt.show()

def plot_exercise_by_smoker():
    plt.figure(figsize=(8,5))
    sns.boxplot(x="Smoker", y="Exercise_Hours_per_Week", data=df, palette="Set3")
    plt.title("Exercise Hours per Week by Smoker Status")
    plt.show()


def plot_sleep_distribution():
    plt.figure(figsize=(8,5))
    sns.histplot(df['Hours_of_Sleep'], bins=15, kde=True, color="orange")
    plt.title("Sleep Hours Distribution")
    plt.xlabel("Hours Slept")
    plt.ylabel("Count")
    plt.show()

def plot_heatmap():
    plt.figure(figsize=(10,7))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

def plot_bmi_by_gender():
    plt.figure(figsize=(8,5))
    sns.boxplot(x="Gender", y="BMI", data=df, palette="Set2")
    plt.title("BMI by Gender")
    plt.show()

def plot_steps_vs_bmi():
    plt.figure(figsize=(8,5))
    sns.scatterplot(x="Daily_Steps", y="BMI", data=df, hue="Gender")
    plt.title("Daily Steps vs BMI")
    plt.show()

def plot_pairplot():
    plt.figure(figsize=(10,7))
    sns.pairplot(df, hue="Gender", palette="Set2", diag_kind="kde")
    plt.suptitle("Pairplot of Numeric Features", y=1.02)
    plt.show()
