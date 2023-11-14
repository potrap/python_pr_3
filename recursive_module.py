def recursive_display(employees, index=0):
    if index < len(employees):
        print(list(employees.keys())[index])
        recursive_display(employees, index + 1)

def recursive_search(employees, name, index=0):
    if index < len(employees):
        current_name = list(employees.keys())[index]
        if current_name.lower() == name.lower():
            return current_name
        else:
            return recursive_search(employees, name, index + 1)
