import pandas as pd
import matplotlib.pyplot as plt
def food_quantity():

    file_path = r"food_wastage_sheet.xlsx"

    df = pd.read_excel(file_path)

    df.columns = df.columns.str.strip()

    required_columns = ['Total Food Prepared (kg)', 'Food Served (kg)', 'Food Wasted (kg)']
    for col in required_columns:
        if col not in df.columns:
            print(f"Error: '{col}' column not found in the dataset!")
            print("Available columns:", df.columns)
            exit()

    total_prepared = df['Total Food Prepared (kg)'].sum()
    total_consumed = df['Food Served (kg)'].sum()
    total_wasted = df['Food Wasted (kg)'].sum()

    labels = ['Food Consumed', 'Food Wasted']
    sizes = [total_consumed, total_wasted]
    colors = ['#2E8B57', '#FF6347']

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
    plt.title("Food Consumption vs Wastage")
    plt.show()
food_quantity()