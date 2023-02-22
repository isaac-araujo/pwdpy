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

    def generate_password(self):
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
        raise ValueError("quantity must be greater than zero")
    if length < 1:
        raise ValueError("length must be greater than zero")
    if not punctuation and not digits and not letters:
        raise ValueError(
            "at least one of this argument must be True (punctuation, digits, letters)"
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

    return password_gen.generate_password()


def __show_error(msg=""):
    print(f"pwdpy error: {msg}", file=sys.stderr)


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Tools for passwords")

    parser.add_argument(
        "-l",
        "--length",
        help="the length of the password (default: 8)",
        type=int,
        default=8,
    )

    parser.add_argument(
        "-q",
        "--quantity",
        help="quantity of passwords to generate (default: 1)",
        type=int,
        default=1,
    )

    parser.add_argument(
        "-p",
        "--punctuation",
        help="use punctuation characters (default: False)",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-d",
        "--digits",
        help="use digits (default: False)",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-le",
        "--letters",
        help="use letter (default: False)",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-nu",
        "--no-upper",
        help="don't use upper case letters (default: False)",
        action="store_false",
        default=True,
        dest="upper",
    )

    parser.add_argument(
        "-nl",
        "--no-lower",
        help="don't use lower case letters (default: False)",
        action="store_false",
        default=True,
        dest="lower",
    )

    args = parser.parse_args()

    try:
        print(
            generate(
                args.quantity,
                length=args.length,
                punctuation=args.punctuation,
                digits=args.digits,
                letters=args.letters,
                l_upper=args.upper,
                l_lower=args.lower,
                charset="",
            )
        )
    except Exception as error_msg:
        __show_error(error_msg.args[0])
