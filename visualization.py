import matplotlib.pyplot as plt
import seaborn as sns
from Dataset import df
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches
import pandas as pd
    
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

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

def plot_health_dashboard():
    fig = plt.figure(figsize=(16, 6))  
    gs = GridSpec(1, 3, figure=fig, wspace=0.4) 
    ax1 = fig.add_subplot(gs[0, 0])
    sns.scatterplot(x='Age', y='BMI', hue='Gender', data=df, ax=ax1)
    ax1.set_title('Age vs BMI', fontsize=13)
    ax2 = fig.add_subplot(gs[0, 1])
    sns.kdeplot(data=df, x='Hours_of_Sleep', y='Exercise_Hours_per_Week',
                cmap='Purples', fill=True, ax=ax2)
    ax2.set_title('Sleep vs Exercise Hours', fontsize=13)
    ax3 = fig.add_subplot(gs[0, 2])
    ax3 = fig.add_subplot(gs[0, 2])
    sns.boxplot(x='Gender', y='Daily_Steps', data=df, ax=ax3)
    ax3.set_title('Daily Steps by Gender', fontsize=13)
    plt.tight_layout()
    fig.suptitle('Simplified Health Dashboard', fontsize=16, weight='bold', y=1.02)
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

# Additional Basic Distributions
def plot_steps_distribution():
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df['Daily_Steps'], bins=20, kde=True, color="purple")
    plt.title("Daily Steps Distribution")
    plt.xlabel("Daily Steps")
    plt.ylabel("Count")
    plt.tight_layout()
    return fig

def plot_heart_rate_distribution():
    fig = plt.figure(figsize=(8,5))
    sns.histplot(df['Heart_Rate'], bins=15, kde=True, color="crimson")
    plt.title("Heart Rate Distribution")
    plt.xlabel("Heart Rate (bpm)")
    plt.ylabel("Count")
    plt.tight_layout()
    return fig

# Additional Comparative Analysis
def plot_sleep_by_age_group():
    # Create age groups
    df['Age_Group'] = pd.cut(df['Age'], bins=[0, 30, 50, 70, 100], labels=['<30', '30-50', '50-70', '70+'])
    
    fig = plt.figure(figsize=(10,6))
    sns.boxplot(x="Age_Group", y="Hours_of_Sleep", data=df, palette="viridis")
    plt.title("Sleep Hours by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Hours of Sleep")
    plt.tight_layout()
    return fig

def plot_heart_rate_by_diabetic():
    fig = plt.figure(figsize=(8,5))
    sns.boxplot(x="Diabetic", y="Heart_Rate", data=df, palette="RdYlBu")
    plt.title("Heart Rate by Diabetic Status")
    plt.xlabel("Diabetic Status")
    plt.ylabel("Heart Rate (bpm)")
    plt.tight_layout()
    return fig

# Additional Correlation Analysis
def plot_health_metrics_heatmap():
    health_metrics = ['BMI', 'Heart_Rate', 'Blood_Pressure', 'Hours_of_Sleep', 'Exercise_Hours_per_Week']
    
    # Extract systolic and diastolic blood pressure
    df['Systolic'] = df['Blood_Pressure'].apply(lambda x: int(x.split('/')[0]))
    df['Diastolic'] = df['Blood_Pressure'].apply(lambda x: int(x.split('/')[1]))
    
    metrics_df = df[['BMI', 'Heart_Rate', 'Systolic', 'Diastolic', 'Hours_of_Sleep', 'Exercise_Hours_per_Week']]
    
    fig = plt.figure(figsize=(10,8))
    sns.heatmap(metrics_df.corr(), annot=True, cmap="YlGnBu", linewidths=0.5)
    plt.title("Health Metrics Correlation Heatmap")
    plt.tight_layout()
    return fig

def plot_lifestyle_vital_correlation():
    # Lifestyle factors and vital signs
    lifestyle = ['Daily_Steps', 'Calories_Intake', 'Exercise_Hours_per_Week', 'Alcohol_Consumption_per_Week']
    
    # Extract systolic and diastolic blood pressure
    df['Systolic'] = df['Blood_Pressure'].apply(lambda x: int(x.split('/')[0]))
    df['Diastolic'] = df['Blood_Pressure'].apply(lambda x: int(x.split('/')[1]))
    
    vitals = ['Heart_Rate', 'Systolic', 'Diastolic', 'BMI']
    
    fig = plt.figure(figsize=(10,8))
    lifestyle_vital_df = df[lifestyle + vitals]
    sns.heatmap(lifestyle_vital_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Lifestyle vs Vital Signs Correlation")
    plt.tight_layout()
    return fig

def plot_age_health_correlation():
    health_indicators = ['Age', 'BMI', 'Heart_Rate', 'Hours_of_Sleep', 'Exercise_Hours_per_Week']
    
    fig = plt.figure(figsize=(12,8))
    corr_matrix = df[health_indicators].corr()
    mask = np.zeros_like(corr_matrix)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr_matrix, mask=mask, annot=True, cmap="YlOrRd", linewidths=0.5)
    plt.title("Age vs Health Indicators Correlation")
    plt.tight_layout()
    return fig

def plot_exercise_impact_correlation():
    impact_vars = ['Exercise_Hours_per_Week', 'BMI', 'Heart_Rate', 'Hours_of_Sleep', 'Daily_Steps']
    
    fig = plt.figure(figsize=(10,6))
    impact_df = df[impact_vars]
    sns.heatmap(impact_df.corr(), annot=True, cmap="PuBu", linewidths=0.5)
    plt.title("Exercise Impact on Health Metrics")
    plt.tight_layout()
    return fig

# Additional Multivariate Analysis
def plot_sleep_vs_exercise():
    fig = plt.figure(figsize=(10,6))
    sns.scatterplot(x="Hours_of_Sleep", y="Exercise_Hours_per_Week", hue="Gender", size="Age", 
                    sizes=(20, 200), palette="viridis", data=df)
    plt.title("Sleep Hours vs Exercise Hours")
    plt.xlabel("Hours of Sleep")
    plt.ylabel("Exercise Hours per Week")
    plt.tight_layout()
    return fig

def plot_calories_vs_weight():
    fig = plt.figure(figsize=(10,6))
    sns.scatterplot(x="Calories_Intake", y="Weight_kg", hue="Gender", style="Smoker", 
                   size="Age", sizes=(30, 200), data=df)
    plt.title("Calorie Intake vs Weight")
    plt.xlabel("Daily Calorie Intake")
    plt.ylabel("Weight (kg)")
    plt.tight_layout()
    return fig

# Additional Advanced Visualizations
def plot_facetgrid_metrics_by_gender():
    g = sns.FacetGrid(df, col="Gender", height=5, aspect=1.2)
    g.map_dataframe(sns.scatterplot, x="BMI", y="Heart_Rate", hue="Smoker", size="Age", sizes=(20, 200), alpha=0.7)
    g.add_legend()
    g.set_axis_labels("BMI", "Heart Rate")
    g.set_titles("{col_name} Gender")
    g.fig.suptitle("Health Metrics by Gender", y=1.05)
    plt.tight_layout()
    return g.fig

def plot_health_radar_chart():
    # Create radar chart comparing multiple people
    fig = plt.figure(figsize=(12, 8))
    
    # Standardize values for better comparison
    categories = ['BMI', 'Daily_Steps', 'Hours_of_Sleep', 'Heart_Rate', 'Exercise_Hours_per_Week']
    
    # Standardize the data for better comparison
    df_std = df.copy()
    for cat in categories:
        df_std[cat] = (df[cat] - df[cat].min()) / (df[cat].max() - df[cat].min())
    
    # Number of people to compare
    num_people = min(3, len(df))
    
    # Set up the radar chart
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # Close the loop
    
    ax = fig.add_subplot(111, polar=True)
    
    # Plot each person
    colors = ['blue', 'green', 'red']
    for i in range(num_people):
        values = df_std.loc[i, categories].values.flatten().tolist()
        values += values[:1]  # Close the loop
        
        ax.plot(angles, values, linewidth=2, color=colors[i], label=f"Person {df.loc[i, 'ID']}")
        ax.fill(angles, values, color=colors[i], alpha=0.25)
    
    # Set the labels and title
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Comparative Health Radar Chart")
    plt.legend(loc='upper right')
    
    plt.tight_layout()
    return fig

def plot_risk_factors_sunburst():
    # Define risk categories
    df['BMI_Category'] = pd.cut(df['BMI'], 
                               bins=[0, 18.5, 25, 30, 100], 
                               labels=['Underweight', 'Normal', 'Overweight', 'Obese'])
    
    # Create a figure for sunburst chart
    fig = plt.figure(figsize=(12, 12))
    
    # Create data for sunburst
    grouped = df.groupby(['Gender', 'Smoker', 'BMI_Category']).size().reset_index(name='Count')
    
    # Set up colors
    colors = plt.cm.tab20.colors
    
    # Create outer ring: Gender
    outer_vals = grouped.groupby('Gender')['Count'].sum()
    outer_labels = outer_vals.index
    
    # Create middle ring: Smoker status
    mid_vals = grouped.groupby(['Gender', 'Smoker'])['Count'].sum().values
    mid_labels = [f"{g} - {s}" for g, s in grouped.groupby(['Gender', 'Smoker']).groups.keys()]
    
    # Create inner ring: BMI Category
    inner_vals = grouped['Count'].values
    inner_labels = [f"{g} - {s} - {b}" for g, s, b in zip(grouped['Gender'], grouped['Smoker'], grouped['BMI_Category'])]
    
    # Create the plot
    ax = fig.add_subplot(111)
    
    # Create the pie chart rings
    ax.pie(outer_vals, radius=1.3, labels=outer_labels, 
           colors=colors[:len(outer_vals)], 
           wedgeprops=dict(width=0.3, edgecolor='w'))
    
    ax.pie(mid_vals, radius=1.0, labels=None,
           colors=colors[len(outer_vals):len(outer_vals)+len(mid_vals)], 
           wedgeprops=dict(width=0.3, edgecolor='w'))
    
    ax.pie(inner_vals, radius=0.7, labels=None,
           colors=colors[len(outer_vals)+len(mid_vals):], 
           wedgeprops=dict(width=0.3, edgecolor='w'))
    
    ax.set_title("Health Risk Factors Sunburst Chart", pad=20)
    
    # Add legend
    plt.legend(title="Categories", loc="center left", bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    return fig

def plot_3d_health_analysis():
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract systolic blood pressure
    df['Systolic'] = df['Blood_Pressure'].apply(lambda x: int(x.split('/')[0]))
    
    # Set up colors based on gender
    colors = {'Male': 'blue', 'Female': 'red'}
    genders = df['Gender'].unique()
    
    # Plot 3D scatter
    for gender in genders:
        subset = df[df['Gender'] == gender]
        ax.scatter(subset['Age'], subset['BMI'], subset['Heart_Rate'],
                   c=subset['Gender'].map(colors), label=gender, s=100, alpha=0.7)
    
    # Add labels
    ax.set_xlabel('Age')
    ax.set_ylabel('BMI')
    ax.set_zlabel('Heart Rate')
    ax.set_title('3D Health Analysis: Age, BMI, and Heart Rate')
    
    # Add legend
    ax.legend()
    
    plt.tight_layout()
    return fig

