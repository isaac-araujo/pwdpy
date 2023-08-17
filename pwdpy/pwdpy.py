import math
import random
import secrets
import sys
from typing import List, Union

from .cli_args import ArgParser
from .contants import *
from .strings import strings


class Charset:
    def __init__(self, charset, min=1):
        self.charset = charset
        self.min = min
        self.count = 0
        self._min_ok = False
        self._timeout = False

    @property
    def min_ok(self):
        return self.count >= self.min


class Password:
    def __init__(self):
        self.charsets = []
        self.minimum_achieved = False
        self.password = ""

    def generate(
        self,
        quantity=1,
        length=12,
        special_characters=True,
        digits=True,
        letters=True,
        l_upper=True,
        l_lower=True,
        charsets=[],
        charset_file="",
        output_file="",
        enconding_file="utf-8",
    ) -> Union[str, List[str]]:
        """Generates a secrets password based on the arguments.

        Args:
            quantity (int, optional): Quantity of passwords to be generate.
                If more than 1 return a list. Defaults to 1.
            length (int, optional): Password length. Defaults to 8.
            special_characters (bool, optional): Whether to use special_characters or not. Defaults to True.
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
            not special_characters
            and not digits
            and not letters
            and not charsets
            and not charset_file
        ):
            raise ValueError(
                "at least one of this argument must exists(special_characters, digits, letters, charset, charset_file)"
            )
        if not isinstance(charsets, list):
            raise ValueError("charset must be a list")

        self.length = length

        if charsets:
            for cs in charsets:
                self.add_charset(Charset(cs))

        elif charset_file:
            with open(charset_file, encoding=enconding_file) as file:
                self.add_charset(Charset(file.read()))

        else:
            if special_characters:
                self.add_charset(Charset(strings.special_characters))
            if digits:
                self.add_charset(Charset(strings.digits))
            if letters:
                if l_upper:
                    self.add_charset(Charset(strings.ascii_uppercase))
                if l_lower:
                    self.add_charset(Charset(strings.ascii_lowercase))
        if quantity > 1:
            password_list = []
            for _ in range(quantity):
                password_list.append(self._generate_password())
            ret = password_list
        else:
            ret = self._generate_password()

        if output_file:
            ret = _export_passwords(output_file, ret)

        return ret

    def add_charset(self, charset: Charset):
        self.charsets.append(charset)

    def add_all_charsets(self):
        self.add_charset(Charset(strings.special_characters))
        self.add_charset(Charset(strings.digits))
        self.add_charset(Charset(strings.ascii_uppercase))
        self.add_charset(Charset(strings.ascii_lowercase))

    def reset_charset(self):
        for charset in self.charsets:
            charset.count = 0
            charset._timeout = False

    def _generate_password(self):
        password = []
        for _ in range(self.length):
            password.append(self._generate_char())

        self.reset_charset()
        return "".join(password)

    def _generate_char(self):
        if not self.minimum_achieved:
            pool = [cs for cs in self.charsets if not cs.min_ok]
            if not pool:
                self.minimum_achieved = True
                return self._generate_char()

            charset = secrets.choice(pool)
            charset.count += 1

        elif len(self.charsets) > 1:
            # guarantees that will not select the same charset twice in a roll
            pool = [cs for cs in self.charsets if not cs._timeout]
            charset = secrets.choice(pool)
            self.reset_charset()
            charset._timeout = True

        else:
            charset = self.charsets[0]

        if (char := secrets.choice(charset.charset)) in self.password:
            # choice again if char alredy in the password
            char = secrets.choice(charset.charset)
        return char


def _export_passwords(output_file, passwords):
    with open(output_file, "w") as file:
        if isinstance(passwords, str):
            passwords = [passwords]
        for pwd in passwords:
            file.writelines(pwd + "\n")
        return True


def generate(
    quantity=1,
    length=12,
    special_characters=True,
    digits=True,
    letters=True,
    l_upper=True,
    l_lower=True,
    charsets=[],
    charset_file="",
    output_file="",
    **kwargs,
) -> Union[str, list]:
    """Generates a secrets password based on the arguments.

    Args:
        quantity (int, optional): Quantity of passwords to be generate.
            If more than 1 return a list. Defaults to 1.
        length (int, optional): Password length. Defaults to 8.
        special_characters (bool, optional): Whether to use special_characters or not. Defaults to True.
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
    password = Password()
    return password.generate(
        quantity,
        length,
        special_characters,
        digits,
        letters,
        l_upper,
        l_lower,
        charsets,
        charset_file,
        output_file,
        **kwargs,
    )


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
    special_characters = False
    ascii_extended = False

    for letter in set(password):
        if letter in strings.ascii_lowercase:
            lowercase = True
        elif letter in strings.ascii_uppercase:
            uppercase = True
        elif letter in strings.digits:
            digits = True
        elif letter in strings.special_characters:
            special_characters = True
        elif letter in strings.ascii_extended:
            ascii_extended = True

    pool_size = 0
    if lowercase:
        pool_size += len(strings.ascii_lowercase)
    if uppercase:
        pool_size += len(strings.ascii_uppercase)
    if digits:
        pool_size += len(strings.digits)
    if special_characters:
        pool_size += len(strings.special_characters)
    if ascii_extended:
        pool_size += len(strings.ascii_extended)

    # Shannon formula
    return round(len(password) * math.log(pool_size, 2), 2)


def strengthen(password: str, shuffle=False, increase=True, max_prefix=5, max_sufix=5) -> str:
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
        try:
            password = str(password)
        except Exception:
            raise TypeError("invalid password format")

    if not isinstance(max_prefix, int):
        raise TypeError("max_prefix must be an integer")
    if not isinstance(max_sufix, int):
        raise TypeError("max_sufix must be an integer")

    stronger_password = ""

    for char in password:
        if (rand_char := _find_related(char)) in stronger_password:
            rand_char = _find_related(char)
        stronger_password += rand_char

    if increase:
        password = Password()
        password.add_all_charsets()

        if max_prefix > 0:
            # adding prefix
            password.length = random.randint(1, max_prefix)
            stronger_password = password._generate_password() + stronger_password

        if max_sufix > 0:
            # adding suffix
            password.length = random.randint(1, max_sufix)
            stronger_password = stronger_password + password._generate_password()

    if shuffle:
        return "".join(random.sample(stronger_password, len(stronger_password)))

    return stronger_password


def _find_related(char):
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
) -> Union[str, list]:
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
            password += f"{_aplly_case(word.strip(), case)}{sep}"
        password_list.append(password.rstrip(sep))

    file.close()

    if len(password_list) == 1:
        return password_list[0]
    else:
        return password_list


def _aplly_case(word, case) -> str:
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
        if args.command in GENERATE:
            result = generate(
                quantity=args.quantity,
                length=args.length,
                special_characters=args.special_characters,
                digits=args.digits,
                letters=args.letters,
                l_upper=args.upper,
                l_lower=args.lower,
                charset_file=args.charset_file,
                output_file=args.output,
            )
            if result:
                if args.output:
                    print(f"Successfully Created: {args.output}")
                else:
                    print(result)

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

        elif args.command in WORDLIST:
            print(
                generate_wordlist(
                    quantity=args.quantity,
                    length=args.length,
                    language=args.language,
                    sep=args.sep,
                    case=args.case,
                    wordlist=args.wordlist,
                )
            )

    except Exception as error_msg:
        _show_error(error_msg.args[-1])


def _show_error(msg=""):
    print(f"pwdpy error: {msg}", file=sys.stderr)


if __name__ == "__main__":
    main()
