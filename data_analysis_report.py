import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def data_analysis_report(file_path, output_dir):
    # Load the dataset
    df = pd.read_excel(file_path)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Descriptive Statistics
    descriptive_stats = df.describe()
    print("Descriptive Statistics:\n", descriptive_stats)
    
    # Data Visualization
    # Age distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=10, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, 'age_distribution.png'))
    plt.close()

    # Salary distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Salary'], bins=10, kde=True)
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, 'salary_distribution.png'))
    plt.close()

    # Department count
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Department', data=df)
    plt.title('Department Count')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.savefig(os.path.join(output_dir, 'department_count.png'))
    plt.close()

    # Correlation Analysis
    # Select only numeric columns for correlation matrix
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    correlation_matrix = df[numeric_cols].corr()
    print("Correlation Matrix:\n", correlation_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
    plt.close()

    # Department-wise Analysis
    # Select numeric columns for groupby mean calculation
    numeric_df = df.select_dtypes(include=[np.number])
    numeric_df['Department'] = df['Department']
    department_stats = numeric_df.groupby('Department').mean()
    print("Department-wise Statistics:\n", department_stats)

    # Boxplot of Salary by Department
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Department', y='Salary', data=df)
    plt.title('Salary Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Salary')
    plt.savefig(os.path.join(output_dir, 'salary_by_department.png'))
    plt.close()

    # Count of employees by Department
    plt.figure(figsize=(10, 6))
    df['Department'].value_counts().plot(kind='bar')
    plt.title('Number of Employees by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    plt.savefig(os.path.join(output_dir, 'employees_by_department.png'))
    plt.close()

    # Trend Analysis
    df['Year'] = df['Joining_Date'].dt.year
    df['Month'] = df['Joining_Date'].dt.month

    plt.figure(figsize=(10, 6))
    df['Year'].value_counts().sort_index().plot(kind='line', marker='o')
    plt.title('Trend of New Joiners by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of New Joiners')
    plt.savefig(os.path.join(output_dir, 'trend_new_joiners_by_year.png'))
    plt.close()

    plt.figure(figsize=(10, 6))
    df.groupby('Year')['Salary'].mean().plot(kind='line', marker='o')
    plt.title('Average Salary Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Salary')
    plt.savefig(os.path.join(output_dir, 'average_salary_over_years.png'))
    plt.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 data_analysis_report.py <path_to_excel_file> <output_directory>")
        sys.exit(1)

    file_path = sys.argv[1]  # Path to your Excel file
    output_dir = sys.argv[2]  # Output directory for saving images
    data_analysis_report(file_path, output_dir)