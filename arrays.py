import pandas as pd
import matplotlib.pyplot as plt

# Use a raw string for the file path
file_path = r"C:\Users\mohan\Downloads\ds_salaries.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Group the data by job title and experience level, calculating the mean salary in USD
job_salary_avg = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
exp_salary_avg = data.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)

# Create bar plot for job title vs average salary
plt.figure(figsize=(10, 6))
job_salary_avg.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Job Title (USD)')
plt.xlabel('Job Title')
plt.ylabel('Average Salary (USD)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Create bar plot for experience level vs average salary
plt.figure(figsize=(6, 4))
exp_salary_avg.plot(kind='bar', color='lightgreen')
plt.title('Average Salary by Experience Level (USD)')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary (USD)')
plt.tight_layout()
plt.show()
