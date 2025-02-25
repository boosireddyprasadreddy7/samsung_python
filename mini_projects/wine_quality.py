import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv(r"C:\Users\boosi\Documents\sic_brpr\samsung_python\mini_projects\wine.csv")


# Convert quality scores (e.g., quality ≥ 7 as good wine)
df["quality_label"] = df["quality"].apply(lambda x: 1 if x >= 7 else 0)

# Train-test split
X = df.drop(["quality", "quality_label"], axis=1)
y = df["quality_label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions & Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
