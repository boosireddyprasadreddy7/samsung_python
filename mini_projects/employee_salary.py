import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\boosi\Documents\sic_brpr\samsung_python\mini_projects\employee.csv")


# Fill missing values
df = df.dropna(subset=['Gender', 'Team'])

# Salary Distribution Per Team
plt.figure(figsize=(10, 5))
sns.barplot(x="Team", y="Salary", data=df, palette="viridis")
plt.xticks(rotation=45)
plt.title("Salary Distribution per Team")
plt.show()
