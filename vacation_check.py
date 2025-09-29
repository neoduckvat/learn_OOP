class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# Класс фуллтайм сотрудника
class FullTimeEmployee(Employee):
    vacation_days = 28

    def get_unpaid_vacation(self, start_date, days):
        return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'

# Класс парт-тайм сотрудника
class PartTimeEmployee(Employee):
    vacation_days = 14

# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
print(full_time_employee.get_vacation_details())

part_time_employee = PartTimeEmployee('Яша', 'Лава', 'ж')
print(part_time_employee.get_vacation_details())
