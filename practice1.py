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

rotary_phone = Phone(dial_type_value='дисковый')
rotary_phone.ring()
rotary_phone.call('14-88')
rotary_phone.get_missed_calls()