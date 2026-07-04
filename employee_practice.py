import pandas as pd

df = pd.read_csv("employee.csv")

def show_menu():
    print("1. Show all employees")
    print("2. IT employees")
    print("3. HR employees")
    print("4. Finance employees")
    print("5. Average salary by department")
    print("6. Highest salary by department")
    print("7. Lowest salary by department")
    print("8. Employee count by department")
    print("9. Exit")

def Show_all_employees():
    return df

def IT_employees():
    return df[df["department"] == "IT"]

def HR_employees():
    return df[df["department"] == "HR"]

def finance_employees():
    return df[df["department"] == "Finance"]

def average_salary_by_department():
    return df.groupby("department")["salary"].mean()

def Highest_salary_by_department():
    return df.groupby("department")["salary"].max()

def lowest_salary_by_department():
    return df.groupby("department")["salary"].min()

def employee_count_by_department():
    return df.groupby("department").size()

operations = {
    "1": Show_all_employees,
    "2": IT_employees,
    "3": HR_employees,
    "4": finance_employees,
    "5": average_salary_by_department,
    "6": Highest_salary_by_department,
    "7": lowest_salary_by_department,
    "8": employee_count_by_department
}

def main():
    while True:
        show_menu()

        choice = input("Choose: ")

        if choice == "9":
            print("Goodbye")
            break

        if choice not in operations:
            print("Invalid choice")
            continue

        result = operations[choice]()
        print(result)

main()