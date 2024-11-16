import employee
def test_get_employees_with_name_starting():
    result = employee.get_employees_with_name_starting("A")
    expect=[{"name": "Alice", "age": 30, "department": "Sales", "salary": 50000}]
    assert result==expect
def test_get_average_age_of_department():
    result= employee.get_average_age_of_department("Sales")
    expect = 27.5
    assert result == expect
def test_get_employee_with_highest_salary():
    result = employee.get_employee_with_highest_salary()
    expect = expect = {"name": "Diana", "age": 35, "department": "Engineering", "salary": 80000}
    assert result == expect