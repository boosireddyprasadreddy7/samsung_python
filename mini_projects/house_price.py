import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\boosi\Documents\sic_brpr\samsung_python\mini_projects\house.csv")


# Price vs. Square Footage
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["SqFt"], y=df["Price"], alpha=0.6, color="red")
plt.title("Price vs. Square Footage")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()
