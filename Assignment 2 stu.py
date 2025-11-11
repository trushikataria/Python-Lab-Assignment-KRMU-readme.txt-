students = {}

def add_student(name, grades):
    students[name] = grades

def avg(grades):
    return sum(grades)/len(grades)

while True:
    print("\n1. Add Student\n2. Show Students\n3. Exit")
    ch = input("Enter choice: ")
    
    if ch == "1":
        name = input("Enter name: ")
        grades = list(map(int, input("Enter grades: ").split()))
        add_student(name, grades)
    elif ch == "2":
        for n,g in students.items():
            print(n, g, "Avg:", avg(g))
    elif ch == "3":
        break
    else:
        print("Invalid choice")