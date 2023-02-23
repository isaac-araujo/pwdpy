import sys
import string
import secrets


class Charset:
    def __init__(self, charset, max, min=1):
        self.charset = charset
        self.max = max
        self.min = min
        self.count = 0
        self._min_ok = False
        self.timeout = False
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
        self.password = []

    def add_charset(self, charset):
        self.charsets.append(charset)

    def reset_charset(self):
        for charset in self.charsets:
            charset.count = 0
            charset.timeout = False

    def generate_password(self):
        self.password = []
        for _ in range(self.length):
            self.password.append(self.__generate_char())
        # secrets.shuffle(self.password)

        self.reset_charset()
        return "".join(self.password)

    def __generate_char(self):
        if not self.minimum_achieved:
            pool = [cs for cs in self.charsets if not cs.min_ok]
            if not pool:
                self.minimum_achieved = True
                return self.__generate_char()

            charset = secrets.choice(pool)
            charset.count += 1

        elif len(self.charsets) > 1:
            # guarantees that will not select the same charset twice in a roll
            pool = [cs for cs in self.charsets if not cs.timeout]
            charset = secrets.choice(pool)
            self.reset_charset()
            charset.timeout = True

        else:
            charset = self.charsets[0]

        if (char := secrets.choice(charset.charset)) in self.password:
            # choice again if char alredy in the password
            char = secrets.choice(charset.charset)
        return char


def generate(
    quantity=1,
    length=8,
    punctuation=True,
    digits=True,
    letters=True,
    l_upper=True,
    l_lower=True,
    charsets=[],
    charset_file="",
    **kwargs,
) -> (str | list):
    """Generates a secrets password based on the arguments.

    Args:
        quantity (int, optional): Quantity of passwords to be generate.
            If more than 1 return a list. Defaults to 1.
        length (int, optional): Password length. Defaults to 8.
        punctuation (bool, optional): Whether to use punctuation or not. Defaults to True.
        digits (bool, optional): Whether to use digits or not. Defaults to True.
        letters (bool, optional): Whether to use letters or not. Defaults to True.
        l_upper (bool, optional): Whether to use uppercase letters or not. Defaults to True.
        l_lower (bool, optional): Whether to use lowercase letters or not. Defaults to True.
        charsets (list, optional): The charsets that will be used instead of the arguments specification. Defaults to [].
        charset_file (str, optional): The charset file will be used instead of the arguments specification. Defaults to "".

    Returns:
        str | list: return a list if the quantity is greater than 1

    """

    if quantity < 1:
        raise ValueError("quantity must be greater than zero")
    if length < 1:
        raise ValueError("length must be greater than zero")
    if (
        not punctuation
        and not digits
        and not letters
        and not charsets
        and not charset_file
    ):
        raise ValueError(
            "at least one of this argument must exists(punctuation, digits, letters, charset, charset_file)"
        )
    if not isinstance(charsets, list):
        raise ValueError("charset must be a list")

    encoding = kwargs.get("encoding", "utf-8")
    password_gen = Password(length)

    if charsets:
        for cs in charsets:
            password_gen.add_charset(Charset(cs, length))

    elif charset_file:
        with open(charset_file, encoding=encoding) as file:
            password_gen.add_charset(Charset(file.read(), length))

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


def test(password: str) -> str:
    ...


def main():
    from . import cli_args

    args = cli_args.get_args()
    try:
        if args.command in cli_args.GENERATE:
            print(
                generate(
                    args.quantity,
                    length=args.length,
                    punctuation=args.punctuation,
                    digits=args.digits,
                    letters=args.letters,
                    l_upper=args.upper,
                    l_lower=args.lower,
                    charset_file=args.charset_file,
                )
            )
        elif args.command in cli_args.TEST:
            print(test(args.password))

    except Exception as error_msg:
        __show_error(error_msg.args[-1])


def __show_error(msg=""):
    print(f"pwdpy error: {msg}", file=sys.stderr)


if __name__ == "__main__":
    main()
