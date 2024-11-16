# Employee data
employee_data = [
    {"name": "Alice", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Bob", "age": 40, "department": "Engineering", "salary": 75000},
    {"name": "Charlie", "age": 28, "department": "HR", "salary": 55000},
    {"name": "Diana", "age": 35, "department": "Engineering", "salary": 80000},
    {"name": "Eve", "age": 25, "department": "Sales", "salary": 47000}
]

def get_employees_with_name_starting(letter):
    """
    This function returns a list of employees whose names start with the given letter (case-insensitive).
    """
    result = []
    for employee in employee_data:
        if employee["name"].lower().startswith(letter.lower()):
            result.append(employee)
    return result


def get_average_age_of_department(department):
    """
    This function calculates the average age of employees in the specified department.
    """
    total_age = 0
    count = 0

    for employee in employee_data:
        if employee["department"].lower() == department.lower():
            total_age += employee["age"]
            count += 1

    average_age = total_age / count if count > 0 else 0
    return average_age


def get_employee_with_highest_salary():
    """
    This function finds the employee with the highest salary.
    """
    highest_salary_employee = None
    highest_salary = float('-inf')

    for employee in employee_data:
        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_salary_employee = employee

    return highest_salary_employee


def main():
    while True:
        print("\n--- Employee Information System ---")
        print("1. Find employees with names starting with a specific letter")
        print("2. Get average age of employees in a department")
        print("3. Find the employee with the highest salary")
        print("Q. Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == '1':
            letter = input("Enter the starting letter of the names: ").strip()
            result = get_employees_with_name_starting(letter)
            print(f"\nEmployees with names starting with '{letter}': {result if result else 'No matches found.'}")
        
        elif choice == '2':
            department = input("Enter the department name: ").strip()
            average_age = get_average_age_of_department(department)
            print(f"\nAverage age of employees in '{department}' department: {average_age:.2f}" if average_age else "No employees found in the specified department.")
        
        elif choice == '3':
            highest_salary_employee = get_employee_with_highest_salary()
            print("\nEmployee with the highest salary:")
            print(highest_salary_employee)
        
        elif choice == 'Q':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
