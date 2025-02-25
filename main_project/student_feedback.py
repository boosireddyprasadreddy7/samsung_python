
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def student_feedback():

    file_path = r"food_wastage_sheet.xlsx"
    df = pd.read_excel(file_path)
    if 'Student Feedback' not in df.columns:
        print("Error: 'Student Feedback' column not found in the dataset!")
        exit()
    feedback_counts = df['Student Feedback'].value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feedback_counts.index, y=feedback_counts.values, palette="coolwarm")
    plt.xlabel("Student Feedback")
    plt.ylabel("Number of Responses")
    plt.title("Student Feedback on Hostel Food")
    plt.xticks(rotation=30, ha='right')
    plt.show()
student_feedback()
