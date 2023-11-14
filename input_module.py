def input_employee_data():
    employees = {}
    while True:
        name = input("Enter employee name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        salary = float(input("Enter employee salary: "))
        days_worked = int(input("Enter number of days worked: "))
        employees[name] = {'salary': salary, 'days_worked': days_worked}
    return employees
