
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def reason_wastage():

    file_path = r"food_wastage_sheet.xlsx"
    df = pd.read_excel(file_path)
    
    if 'Reasons for Waste' not in df.columns:
        print("Error: 'Reasons for Waste' column not found in the dataset!")
        exit()

    waste_reason_counts = df['Reasons for Waste'].value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=waste_reason_counts.index, y=waste_reason_counts.values, palette="viridis")
    plt.xlabel("Reasons for Food Waste")
    plt.ylabel("Number of Occurrences")
    plt.title("Reasons for Food Wastage in Hostels")
    plt.xticks(rotation=30, ha='right')
    plt.show()
reason_wastage()