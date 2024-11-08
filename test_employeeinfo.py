import employee_info

def test_calculate_average_salary():#don't forget to add text in front of the def name
    average= employee_info.calculate_average_salary()
    assert(round(average,2)==60166.67)
    
def test_get_employees_by_age_range():
    lower = 21
    upper = 32
    Expected_Dict= [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    age_range_test=employee_info.get_employees_by_age_range(lower,upper)
    assert age_range_test==Expected_Dict

def test_get_employees_by_dept():
    department_test=employee_info.get_employees_by_dept("Sales")
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ] 
    assert department_test==employee_data
    