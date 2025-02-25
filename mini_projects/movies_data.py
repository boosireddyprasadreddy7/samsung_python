import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\boosi\Documents\sic_brpr\samsung_python\mini_projects\movies.csv")

# Top 10 Highest-Grossing Movies
top_movies = df.nlargest(10, "WorldGross")
plt.figure(figsize=(10, 6))
sns.barplot(y=top_movies["Movie"], x=top_movies["WorldGross"], palette="viridis")
plt.title("Top 10 Highest-Grossing Movies")
plt.xlabel("World Gross (in millions)")
plt.ylabel("Movie")
plt.show()
