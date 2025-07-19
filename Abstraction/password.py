from abc import ABC, abstractmethod
from random import randint, shuffle

class GeneratePassword(ABC):

    @abstractmethod
    def generate(self):
        pass


class CharPassword(GeneratePassword):

    def generate(self):
        password = ""
        lower_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        upper_letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        all_letters = lower_letters + upper_letters
        shuffle(all_letters)

        for i in range(20):
            idx = randint(0, len(all_letters) - 1)
            letter = all_letters[idx]
            password += letter
        return password
    

class DigitPassword(GeneratePassword):

    def generate(self):
        password = ""
        digits = "0123456789"
        shuffle(list(digits))

        for i in range(20):
            idx = randint(0, len(digits) - 1)
            digit = digits[idx]
            password += digit
        return password
    

class HybridPassword(GeneratePassword):

    def generate(self):
        password = ""
        lower_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        upper_letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        all_letters = lower_letters + upper_letters
        digits = list("0123456789")
        all_letters_digits = all_letters + digits
        shuffle(all_letters_digits)

        for i in range(20):
            idx = randint(0, len(all_letters_digits) - 1)
            char = all_letters_digits[idx]
            password += char
        return password




charpwd = CharPassword()
print(charpwd.generate())

digitpwd = DigitPassword()
print(digitpwd.generate())

hybridpwd = HybridPassword()
print(hybridpwd.generate())

