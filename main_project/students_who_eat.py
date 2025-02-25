
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def students_who_eat():
    file_path = r"food_wastage_sheet.xlsx"
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()
    required_columns = ['Hostel Name', 'Number of Residents', 'Number of Students Who Ate']
    for col in required_columns:
        if col not in df.columns:
            print(f"Error: '{col}' column not found in the dataset!")
            print("Available columns:", df.columns)
            exit()
    hostel_data = df.groupby('Hostel Name')[['Number of Residents', 'Number of Students Who Ate']].sum()

    x = np.arange(len(hostel_data.index)) 
    width = 0.35 
    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, hostel_data['Number of Residents'], width, label='Total Residents', color='skyblue', edgecolor='black')
    plt.bar(x + width/2, hostel_data['Number of Students Who Ate'], width, label='Students Who Ate', color='orange', edgecolor='black')

    plt.xlabel("Hostel Name")
    plt.ylabel("Count")
    plt.title("Comparison of Residents vs. Students Who Ate in Each Hostel")
    plt.xticks(ticks=x, labels=hostel_data.index, rotation=45) 
    plt.legend()

    # Show the plot
    plt.show()
students_who_eat()