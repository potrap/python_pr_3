def calculate_salary(employee_data):
    for name, data in employee_data.items():
        salary = (data['salary'] / 30) * data['days_worked']
        bonus = (data['salary'] / 30) * data['days_worked'] * 0.1
        print(f"{name}: Salary - {salary}, Bonus - {bonus}")

def calculate_bonuses(employee_data):
    bonuses = {}
    for name, data in employee_data.items():
        bonus = (data['salary'] / 30) * data['days_worked'] * 0.1
        bonuses[name] = bonus
    return bonuses
