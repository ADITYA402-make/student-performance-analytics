import pandas as pd
import numpy as np



SUBJECTS = [
    "science",
    "Mathematics",
    "English",
    "Computer_Science",
    "History"
    
]


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_result(row):
   
    if all(row[subject] >= 35 for subject in SUBJECTS):
        return "Pass"
    return "Fail"


def analyze_students():
    
    df = pd.read_csv("students.csv")

    
    print("\n===== STUDENT DATASET =====")
    

    print("\nTotal students:", len(df))
    print("Dataset columns:", list(df.columns))

    
    df["Total"] = df[SUBJECTS].sum(axis=1)
    df["Average"] = df[SUBJECTS].mean(axis=1)

    
    df["Grade"] = df["Average"].apply(calculate_grade)
    df["Result"] = df.apply(calculate_result, axis=1)

    
    print("\n===== STUDENT PERFORMANCE =====")
    print(
        df[
            ["Student_ID", "Name", "Total",
             "Average", "Grade", "Result", "Attendance"]
        ].to_string(index=False)
    )

    
    class_average = np.mean(df["Average"].to_numpy())
    highest_average = df["Average"].max()
    lowest_average = df["Average"].min()

    print("\n===== CLASS STATISTICS =====")
    print(f"Class average: {class_average:.2f}")
    print(f"Highest student average: {highest_average:.2f}")
    print(f"Lowest student average: {lowest_average:.2f}")

  
    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()

    print("\nStudents passed:", pass_count)
    print("Students failed:", fail_count)

    
    print("\n===== SUBJECT-WISE ANALYSIS =====")
    subject_averages = df[SUBJECTS].mean()

    for subject, average in subject_averages.items():
        print(f"{subject}: {average:.2f}")

    best_subject = subject_averages.idxmax()
    print("\nBest-performing subject:", best_subject)

    
    print("\n===== TOP 3 STUDENTS =====")
    top_students = df.nlargest(3, "Average")

    print(
        top_students[
            ["Name", "Average", "Grade"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    analyze_students()