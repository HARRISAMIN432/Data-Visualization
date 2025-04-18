import matplotlib.pyplot as plt
import seaborn as sns
from Dataset import df
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches
    
def plot_alcohol_vs_heart_rate():
    fig = plt.figure(figsize=(8,5))
    sns.barplot(x="Alcohol_Consumption_per_Week", y="Heart_Rate", data=df, palette="Blues_d")
    plt.title("Alcohol Consumption vs Heart Rate")
    plt.xlabel("Alcohol Consumption (per Week)")
    plt.ylabel("Heart Rate")
    plt.tight_layout()
    return fig

def plot_alcohol_kde_by_gender():
    fig = plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x="Alcohol_Consumption_per_Week", hue="Gender", fill=True, common_norm=False, alpha=0.5, palette="magma")
    plt.title("Alcohol Consumption Distribution by Gender")
    plt.xlabel("Alcohol Consumption per Week")
    plt.ylabel("Density")
    plt.tight_layout()
    return fig

def plot_advanced_correlation_heatmap():
    fig = plt.figure(figsize=(12, 8))
    corr = df.corr(numeric_only=True)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=.5)
    plt.title("Advanced Correlation Heatmap")
    plt.tight_layout()
    return fig

def plot_bmi_vs_age():
    fig = plt.figure(figsize=(8,5))
    sns.regplot(x="Age", y="BMI", data=df, scatter_kws={'s': 100, 'alpha': 0.5}, line_kws={'color': 'red'})
    plt.title("BMI vs Age with Regression Line")
    plt.xlabel("Age")
    plt.ylabel("BMI")
    plt.tight_layout()
    return fig

def plot_facetgrid_steps_vs_bmi():
    g = sns.FacetGrid(df, col="Gender", height=5, aspect=1.2)
    g.map(sns.scatterplot, "Daily_Steps", "BMI", alpha=0.7)
    g.set_axis_labels("Daily Steps", "BMI")
    g.set_titles("{col_name} Gender")
    g.fig.suptitle("Daily Steps vs BMI by Gender", y=1.05)
    plt.tight_layout()
    return g.fig

def plot_age_distribution():
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=20, kde=True)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.tight_layout()
    return fig

def plot_bmi_vs_smoker_by_gender():
    fig = plt.figure(figsize=(10,6))
    sns.violinplot(x="Smoker", y="BMI", hue="Gender", data=df, split=True, inner="quartile", palette="Pastel1")
    sns.swarmplot(x="Smoker", y="BMI", hue="Gender", data=df, dodge=True, alpha=0.5, color=".2")
    plt.title("BMI Distribution by Smoker Status and Gender")
    plt.xlabel("Smoker")
    plt.ylabel("BMI")
    plt.legend(title="Gender", loc='upper right')
    plt.tight_layout()
    return fig

def plot_bmi_distribution():
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df['BMI'], bins=20, kde=True, color="green")
    plt.title("BMI Distribution")
    plt.xlabel("BMI")
    plt.ylabel("Count")
    plt.tight_layout()
    return fig

def plot_exercise_by_smoker():
    fig = plt.figure(figsize=(8,5))
    sns.boxplot(x="Smoker", y="Exercise_Hours_per_Week", data=df, palette="Set3")
    plt.title("Exercise Hours per Week by Smoker Status")
    plt.tight_layout()
    return fig

def plot_sleep_distribution():
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df['Hours_of_Sleep'], bins=15, kde=True, color="orange")
    plt.title("Sleep Hours Distribution")
    plt.xlabel("Hours Slept")
    plt.ylabel("Count")
    plt.tight_layout()
    return fig

def plot_heatmap():
    fig = plt.figure(figsize=(10,7))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    return fig

def plot_bmi_by_gender():
    fig = plt.figure(figsize=(8,5))
    sns.boxplot(x="Gender", y="BMI", data=df, palette="Set2")
    plt.title("BMI by Gender")
    plt.tight_layout()
    return fig

def plot_steps_vs_bmi():
    fig = plt.figure(figsize=(8,5))
    sns.scatterplot(x="Daily_Steps", y="BMI", data=df, hue="Gender")
    plt.title("Daily Steps vs BMI")
    plt.tight_layout()
    return fig

def plot_pairplot():
    g = sns.pairplot(df, hue="Gender", palette="Set2", diag_kind="kde")
    g.figure.suptitle("Pairplot of Numeric Features", y=1.03)
    g.figure.tight_layout()  
    return g.figure

def plot_clustermap():
    numeric_df = df.select_dtypes(include=["float64", "int64"])
    g = sns.clustermap(numeric_df.corr(), cmap="coolwarm", annot=True)
    plt.title("Clustermap of Feature Correlations")
    return g.fig

def plot_radar_chart(index=0):
    fig = plt.figure(figsize=(6, 6))
    categories = ['BMI', 'Daily_Steps', 'Hours_of_Sleep', 'Heart_Rate', 'Exercise_Hours_per_Week', 'Alcohol_Consumption_per_Week']
    values = df.loc[index, categories].values.flatten().tolist()
    values += values[:1]  
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, color='r', linewidth=2)
    ax.fill(angles, values, color='r', alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title(f"Radar Chart: Profile for Individual {df.loc[index, 'ID']}")
    plt.tight_layout()
    return fig

def plot_health_dashboard():
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 3, figure=fig)    
    ax1 = fig.add_subplot(gs[0, 0])
    sns.scatterplot(x='Age', y='BMI', hue='Gender', data=df, ax=ax1)
    ax1.set_title('Age vs BMI')
    ax2 = fig.add_subplot(gs[0, 1])
    sns.boxplot(x='Gender', y='Daily_Steps', data=df, ax=ax2)
    ax2.set_title('Daily Steps by Gender')    
    ax3 = fig.add_subplot(gs[0, 2])
    sns.kdeplot(data=df, x='Hours_of_Sleep', y='Exercise_Hours_per_Week', 
                cmap='Blues', fill=True, ax=ax3)
    ax3.set_title('Sleep vs Exercise Hours')    
    ax4 = fig.add_subplot(gs[1, :2])
    sns.scatterplot(x='BMI', y='Heart_Rate', size='Age', hue='Smoker', 
                    sizes=(20, 200), data=df, ax=ax4)
    ax4.set_title('Health Risk Matrix (BMI vs Heart Rate)')    
    ax5 = fig.add_subplot(gs[1, 2])
    sns.barplot(x='Smoker', y='Alcohol_Consumption_per_Week', 
                hue='Gender', data=df, ax=ax5)
    ax5.set_title('Alcohol Consumption by Smoking Status')    
    ax6 = fig.add_subplot(gs[2, :])
    sns.heatmap(df.select_dtypes(include=['number']).corr(), 
                annot=True, cmap='coolwarm', ax=ax6)
    ax6.set_title('Feature Correlation Matrix')    
    plt.tight_layout()
    return fig

def plot_sunburst():
    df['Health_Risk'] = np.where((df['BMI'] > 30) | (df['Heart_Rate'] > 90), 
                               'High', 'Low')
    grouped = df.groupby(['Gender', 'Smoker', 'Health_Risk']).size().reset_index(name='Count')
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))    
    colors = {
        ('Male', 'No', 'Low'): 'lightblue',
        ('Male', 'No', 'High'): 'blue',
        ('Male', 'Yes', 'Low'): 'lightgreen',
        ('Male', 'Yes', 'High'): 'green',
        ('Female', 'No', 'Low'): 'pink',
        ('Female', 'No', 'High'): 'red',
        ('Female', 'Yes', 'Low'): 'lightyellow',
        ('Female', 'Yes', 'High'): 'yellow'
    }    
    outer_vals = grouped.groupby('Gender')['Count'].sum()
    wedges_outer, _ = ax.pie(outer_vals, radius=1.3, 
                             colors=['lightblue', 'pink'], 
                             wedgeprops=dict(width=0.3, edgecolor='w'))
    mid_vals = grouped.groupby(['Gender', 'Smoker'])['Count'].sum()
    wedges_mid, _ = ax.pie(mid_vals, radius=1.0, 
                           colors=['lightblue', 'lightgreen', 'pink', 'lightyellow'], 
                           wedgeprops=dict(width=0.3, edgecolor='w'))
    inner_vals = grouped['Count']
    wedges_inner, _ = ax.pie(inner_vals, radius=0.7, 
                             colors=[colors[tuple(x)] for x in grouped[['Gender', 'Smoker', 'Health_Risk']].values], 
                             wedgeprops=dict(width=0.3, edgecolor='w'))    
    ax.set_title("Health Risk Sunburst Chart\n(Gender → Smoking Status → Risk Level)", pad=20)    
    legend_elements = [
        mpatches.Patch(facecolor='lightblue', label='Male'),
        mpatches.Patch(facecolor='pink', label='Female'),
        mpatches.Patch(facecolor='blue', label='Male High Risk'),
        mpatches.Patch(facecolor='green', label='Male Smoker High Risk'),
        mpatches.Patch(facecolor='red', label='Female High Risk'),
        mpatches.Patch(facecolor='yellow', label='Female Smoker High Risk')
    ]
    ax.legend(handles=legend_elements, bbox_to_anchor=(1, 0.5), loc='center left')
    plt.tight_layout()
    return fig