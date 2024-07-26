def calculate_total_payroll(salaries):
    total = 0
    for salary in salaries:
        total += salary
    return total

def find_highest_salary(salaries):
    highest = salaries[0]
    for salary in salaries:
        if salary > highest: # missing colon
            highest = salary
    return highest

def high_earners(employees, salaries, threshold):
    high_earners_list = []
    for i in range(len(employees)):
        if salaries[i] > threshold:
            high_earners_list.append(employees[i])
    return high_earners_list

employees = ["John", "Jane", "Doe", "Emily", "Michael"]
salaries = [50000, 60000, 55000, 70000, 75000]  # 75000 was a str instead of an int
threshold = 60000

total_payroll = calculate_total_payroll(salaries)
print("Total payroll:", total_payroll)

highest_salary = find_highest_salary(salaries)
print("Highest salary:", highest_salary)

high_earners_list = high_earners(employees, salaries, threshold)
print("High earners:", high_earners_list)