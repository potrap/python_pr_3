from input_module import input_employee_data
from calculation_module import calculate_salary, calculate_bonuses
from recursive_module import recursive_display, recursive_search

def main():
    employees = input_employee_data()
    calculate_salary(employees)
    
    name_to_search = input("Enter the name to search: ")
    result = recursive_search(employees, name_to_search)
    if result:
        print(f"Employee {result} found!")
    else:
        print(f"Employee {name_to_search} not found.")

    recursive_display(employees)

if __name__ == "__main__":
    main()
