import string
import random


class Charset:
    def __init__(self, charset, max, min=1):
        self.charset = charset
        self.max = max
        self.min = min
        self.count = 0
        self._min_ok = False
        # self._max_ok = False

    # @property
    # def max_ok(self):
    #     return self.count >= self.max

    @property
    def min_ok(self):
        return self.count >= self.min


class Password:
    def __init__(self, length):
        self.length = length
        self.charsets = []
        self.minimum_achieved = False

    def add_charset(self, charset):
        self.charsets.append(charset)

    def generate(self):
        password = []
        for _ in range(self.length):
            password.append(self.__generate_char())
        random.shuffle(password)
        return "".join(password)

    def __generate_char(self):
        if not self.minimum_achieved:
            pool = [cs for cs in self.charsets if not cs.min_ok]
            if not pool:
                self.minimum_achieved = True
                return self.__generate_char()

            charset = random.choice(pool)
            charset.count += 1
        else:
            charset = random.choice(self.charsets)

        return random.choice(charset.charset)


def generate(
    quantity=1,
    length=8,
    punctuation=True,
    digits=True,
    letters=True,
    l_upper=True,
    l_lower=True,
    charset="",
    **kwargs
) -> (str | list):
    """Generates a random password based on the arguments.

    Args:
        quantity (int, optional): Quantity of passwords to be generate.
            If more than 1 return a list. Defaults to 1.
        length (int, optional): Password length. Defaults to 8.
        punctuation (bool, optional): Whether to use punctuation or not. Defaults to True.
        digits (bool, optional): Whether to use digits or not. Defaults to True.
        letters (bool, optional): Whether to use letters or not. Defaults to True.
        l_upper (bool, optional): Whether to use uppercase letters or not. Defaults to True.
        l_lower (bool, optional): Whether to use lowercase letters or not. Defaults to True.
        charset (str, optional): The charset will be used instead of the arguments specification. Defaults to "".

    Returns:
        str | list: return a list if the quantity is greater than 1

    """

    if quantity < 1:
        raise ValueError("Quantity must be greater than zero")
    if length < 1:
        raise ValueError("Length must be greater than zero")
    if not punctuation and not digits and not letters:
        raise ValueError(
            "At least one that argument must be True (punctuation, digits, letters)"
        )

    password_gen = Password(length)

    if charset:
        password_gen.add_charset(Charset(charset, length))
    else:
        if punctuation:
            password_gen.add_charset(Charset(string.punctuation, length))
        if digits:
            password_gen.add_charset(Charset(string.digits, length))
        if letters:
            if l_upper:
                password_gen.add_charset(Charset(string.ascii_uppercase, length))
            if l_lower:
                password_gen.add_charset(Charset(string.ascii_lowercase, length))
    if quantity > 1:
        password_list = []
        for _ in range(quantity):
            password_list.append(password_gen.generate_password())
        return password_list

    password = password_gen.generate()
    return password
