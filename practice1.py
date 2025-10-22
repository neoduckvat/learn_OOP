class Phone:
    line_type = 'проводной'

    def __init__(self,dial_type_value ):
        self.dial_type = dial_type_value

    def dial_type_upgrade(self, new_dial_type):
        self.dial_type = new_dial_type


    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}')

    def get_missed_calls(self):
        print('Запрос количества пропущенных звонков')

class MobilePhone(Phone):
    pass


mobile_phone = MobilePhone('сенсорный')

mobile_phone.ring()
