"""
GradeBook Analyzer
Author: Ayushi Rai
Date: 2024
Mini Project: Analysing and Reporting Student Grades
"""

import csv
import statistics

# ---------------------- TASK 3: STATISTICAL FUNCTIONS ----------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

# ---------------------- TASK 4: GRADE ASSIGNMENT ----------------------

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_distribution(grades_dict):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades_dict.values():
        dist[g] += 1
    return dist

# ---------------------- TASK 2: DATA INPUT METHODS ----------------------

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Student name: ").strip()
        mark = int(input("Marks: "))
        marks[name] = mark
    return marks

def load_from_csv():
    marks = {}
    filename = input("Enter CSV filename: ")
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header if exists
            for row in reader:
                name, mark = row
                marks[name] = int(mark)
    except FileNotFoundError:
        print("CSV file not found.")
    return marks

# ---------------------- TASK 6: DISPLAY TABLE ----------------------

def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("----------------------------------------")
    for name in marks:
        print(f"{name:12}\t{marks[name]}\t{grades[name]}")
    print()

# ---------------------- MAIN PROGRAM LOOP ----------------------

def main():
    print("\nWelcome to GradeBook Analyzer")
    print("1. Manual data entry")
    print("2. Load from CSV")
    print("3. Exit")

    while True:
        choice = input("\nChoose an option: ")

        if choice == "1":
            marks = manual_input()

        elif choice == "2":
            marks = load_from_csv()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        # Task 3: Statistics
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        print(f"\nAverage Score: {avg:.2f}")
        print(f"Median Score: {med}")
        print(f"Highest Score: {max_name} -> {max_score}")
        print(f"Lowest Score: {min_name} -> {min_score}")

        # Task 4: Grades
        grades = assign_grades(marks)
        dist = grade_distribution(grades)

        print("\nGrade Distribution:")
        for g, cnt in dist.items():
            print(f"{g}: {cnt}")

        # Task 5: Pass/Fail using List Comprehension
        passed = [name for name, m in marks.items() if m >= 40]
        failed = [name for name, m in marks.items() if m < 40]

        print(f"\nPassed ({len(passed)}): {passed}")
        print(f"Failed ({len(failed)}): {failed}")

        # Task 6: Final Table
        print_table(marks, grades)

        again = input("Do you want to run again? (y/n): ").lower()
        if again != "y":
            print("Exiting program...")
            break


if __name__ == "_main_":
    main()