import math
import random
import secrets
from typing import Union

from click import style
from colorama import init

from .cli_args import ArgParser
from .contants import *
from .strings import strings


class Charset:
    def __init__(self, charset, min=1):
        self.charset = charset
        # self.max = max
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
    def __init__(self, length=0):
        self.length = length
        self.charsets = []
        self.minimum_achieved = False
        self.password = []

    def add_charset(self, charset: Charset):
        self.charsets.append(charset)

    def add_all_charsets(self):
        self.add_charset(Charset(strings.punctuation))
        self.add_charset(Charset(strings.digits))
        self.add_charset(Charset(strings.ascii_uppercase))
        self.add_charset(Charset(strings.ascii_lowercase))

    def reset_charset(self):
        for charset in self.charsets:
            charset.count = 0
            charset.timeout = False

    def generate_password(self):
        self.password = []
        for _ in range(self.length):
            self.password.append(self.__generate_char())

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
    length=12,
    punctuation=True,
    digits=True,
    letters=True,
    l_upper=True,
    l_lower=True,
    charsets=[],
    charset_file="",
    output_file="",
    **kwargs,
) -> Union(str, list):
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
        output_file (str, optional): The output file will be created with the passwords.

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
            password_gen.add_charset(Charset(cs))

    elif charset_file:
        with open(charset_file, encoding=encoding) as file:
            password_gen.add_charset(Charset(file.read()))

    else:
        if punctuation:
            password_gen.add_charset(Charset(strings.punctuation))
        if digits:
            password_gen.add_charset(Charset(strings.digits))
        if letters:
            if l_upper:
                password_gen.add_charset(Charset(strings.ascii_uppercase))
            if l_lower:
                password_gen.add_charset(Charset(strings.ascii_lowercase))
    if quantity > 1:
        password_list = []
        for _ in range(quantity):
            password_list.append(password_gen.generate_password())
        ret = password_list
    else:
        ret = password_gen.generate_password()

    if output_file:
        ret = __export_passwords(output_file, ret)

    return ret


def __export_passwords(output_file, passwords):
    with open(output_file, "w") as file:
        if isinstance(passwords, str):
            passwords = [passwords]
        for pwd in passwords:
            file.writelines(pwd + "\n")
        return True


def entropy(password: str) -> float:
    """Return the password entropy using Shannon formula

    Args:
        password (str): password to calculate

    Raises:
        TypeError: password must be a string

    Returns:
        float: calculated entropy
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    lowercase = False
    uppercase = False
    digits = False
    punctuation = False
    ascii_extended = False

    for letter in set(password):
        if letter in strings.ascii_lowercase:
            lowercase = True
        elif letter in strings.ascii_uppercase:
            uppercase = True
        elif letter in strings.digits:
            digits = True
        elif letter in strings.punctuation:
            punctuation = True
        elif letter in strings.ascii_extended:
            ascii_extended = True

    pool_size = 0
    if lowercase:
        pool_size += len(strings.ascii_lowercase)
    if uppercase:
        pool_size += len(strings.ascii_uppercase)
    if digits:
        pool_size += len(strings.digits)
    if punctuation:
        pool_size += len(strings.punctuation)
    if ascii_extended:
        pool_size += len(strings.ascii_extended)

    # Shannon formula
    return round(len(password) * math.log(pool_size, 2), 2)


def strengthen(
    password: str, shuffle=False, increase=True, max_prefix=5, max_sufix=5
) -> str:
    """Fortify the password using related characters

    Args:
        password (str): Password
        increase (bool, optional): Whether the password length will increase or continue the same. Defaults to True.
        shuffle (bool, optional): Shuffle password after strengthen. Defaults to False.
        max_prefix (int, optional): Shuffle password after strengthen. Defaults to False.
        max_sufix (int, optional): Shuffle password after strengthen. Defaults to False.

    Raises:
        TypeError: Password must be a string

    Returns:
        str: Strengthened password
    """

    if not isinstance(password, str):
        raise TypeError("password must be a string")
    if not isinstance(max_prefix, int):
        raise TypeError("max_prefix must be an integer")
    if not isinstance(max_sufix, int):
        raise TypeError("max_sufix must be an integer")

    stronger_password = ""

    for char in password:
        if (rand_char := __find_related(char)) in stronger_password:
            rand_char = __find_related(char)
        stronger_password += rand_char

    if increase:
        password = Password()
        password.add_all_charsets()

        if max_prefix > 0:
            # adding prefix
            password.length = random.randint(1, max_prefix)
            stronger_password = password.generate_password() + stronger_password

        if max_sufix > 0:
            # adding suffix
            password.length = random.randint(1, max_sufix)
            stronger_password = stronger_password + password.generate_password()

    if shuffle:
        return "".join(random.sample(stronger_password, len(stronger_password)))

    return stronger_password


def __find_related(char):
    for pool in strings.related:
        if char == pool[0] or char == pool[1]:
            return secrets.choice(pool)
    return char


def generate_wordlist(
    quantity=1,
    length=8,
    language="english",
    sep=" ",
    case="lower",
    wordlist: str = None,
) -> Union(str, list):
    """_summary_

    Args:
        quantity (int, optional): Quantity of passwords to be generate.
            If more than 1 return a list. Defaults to 1.
        length (int, optional): Quantity of words in the password to be generate. Defaults to 8.
        language (str, optional): Language of the wordlist to use. Defaults to "english".
        sep (str, optional): Separator between words. Defaults to " ".
        case (str, optional): Case that the words will be (lower, upper or title). Defaults to "lower".
        wordlist (str, optional): The path to to the wordlist file. Defaults to None.

    Raises:
        ValueError: Quantity must be greater than zero
        ValueError: Length must be greater than zero
        ValueError: Case must be lower or upper or title
        ValueError: Invalid language

    Returns:
        str | list: if quantity is greater than one return list
    """

    if quantity < 1:
        raise ValueError("quantity must be greater than zero")
    if length < 1:
        raise ValueError("length must be greater than zero")
    if case not in ["lower", "upper", "title"]:
        raise ValueError("case must be lower or upper or title")

    try:
        if wordlist:
            path = wordlist
        else:
            path = f"languages/{language}.txt"

        file = open(path, "r", encoding="utf-8")

    except FileNotFoundError:
        raise ValueError("invalid language")

    words = file.readlines()
    password_list = []
    sep = str(sep)
    for _ in range(quantity):
        password = ""
        for _ in range(length):
            word = secrets.choice(words)
            password += f"{__aplly_case(word.strip(), case)}{sep}"
        password_list.append(password.rstrip(sep))

    file.close()

    if len(password_list) == 1:
        return password_list[0]
    else:
        return password_list


def __aplly_case(word, case) -> str:
    if case == "lower":
        return word.lower()
    if case == "upper":
        return word.upper()
    if case == "title":
        return word.title()

    return word


def main():

    args = ArgParser.get_args()
    try:
        init(convert=True)
        if args.command in GENERATE:
            result = generate(
                args.quantity,
                length=args.length,
                punctuation=args.punctuation,
                digits=args.digits,
                letters=args.letters,
                l_upper=args.upper,
                l_lower=args.lower,
                charset_file=args.charset_file,
                output_file=args.output,
            )
            if args.output:
                if result:

                    print(
                        style(f"Successfully Created:", fg="blue", bold=True),
                        f"{args.output}",
                    )

        elif args.command in ENTROPY:
            print(entropy(password=args.password))

        elif args.command in STRENGTHEN:
            print(
                strengthen(
                    password=args.password,
                    increase=args.increase,
                    shuffle=args.shuffle,
                    max_prefix=args.max_prefix,
                    max_sufix=args.max_sufix,
                )
            )

    except Exception as error_msg:
        __show_error(error_msg.args[-1])


def __show_error(msg=""):
    print(
        style(f"pwdpy error:", fg="red", bold=True),
        f"{msg}",
    )


if __name__ == "__main__":
    main()
