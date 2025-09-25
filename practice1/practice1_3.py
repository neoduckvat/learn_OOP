class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        for letter in original_text.lower():
            if letter in self.alphabet:
                idx = self.alphabet.index(letter)
                result.append(self.alphabet[(idx + shift) % len(self.alphabet)])
            else:
                result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        result = []
        for letter in cipher_text.lower():
            if letter in self.alphabet:
                idx = self.alphabet.index(letter)
                result.append(self.alphabet[(idx - shift) % len(self.alphabet)])
            else:
                result.append(letter)
        return ''.join(result)



cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))