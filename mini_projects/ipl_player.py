import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\boosi\Documents\sic_brpr\samsung_python\mini_projects\IPLData.csv")


# Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)
for col in df.select_dtypes(include=['object']):
    df[col].fillna(df[col].mode()[0], inplace=True)

# Top 5 Run Scorers
top_run_scorers = df[['Player Name', 'Team', 'Runs']].sort_values(by='Runs', ascending=False).head(5)
print(top_run_scorers)

# Plot Top 5 Run Scorers
plt.figure(figsize=(8,5))
sns.barplot(data=top_run_scorers, x="Runs", y="Player Name", palette="viridis")
plt.title("Top 5 Run Scorers in IPL")
plt.show()
