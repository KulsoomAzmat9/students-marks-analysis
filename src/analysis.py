import pandas as pd
import matplotlib.pyplot as plt

# Load light CSV
df = pd.read_csv('data/students_marks.csv')

# Auto calculations (keeps CSV light)
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = round(df['Total'] / 3, 2)

# Grade function
def get_grade(avg):
    if avg >= 90: return 'A+'
    if avg >= 80: return 'A'
    if avg >= 70: return 'B'
    if avg >= 60: return 'C'
    return 'D'

df['Grade'] = df['Average'].apply(get_grade)

# Print results
print("--- Students Marks ---")
print(df.to_string(index=False))
print(f"\nTopper: {df.loc[df['Average'].idxmax(), 'Name']} - {df['Average'].max()}%")
print(f"Class Average: {df['Average'].mean():.2f}%")

# Chart 1: Average marks
plt.figure(figsize=(8,4))
plt.bar(df['Name'], df['Average'], color='#6C8EBF')
plt.title('Students Average Marks')
plt.ylabel('Average')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('charts/avg_chart.png')
print("\nChart saved: charts/avg_chart.png")

# Chart 2: Subject average
plt.figure(figsize=(6,4))
subject_avg = df[['Math','Science','English']].mean()
plt.bar(subject_avg.index, subject_avg.values, color=['#FF9AA2','#A0E7E5','#FFDAC1'])
plt.title('Subject-wise Average')
plt.ylabel('Avg Marks')
plt.tight_layout()
plt.savefig('charts/subject_chart.png')
print("Chart saved: charts/subject_chart.png")