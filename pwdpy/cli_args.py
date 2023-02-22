import argparse


def get_args():
    parser = argparse.ArgumentParser(prog="pwdpy", description="Tools for passwords")

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

    parser.add_argument(
        "-cf",
        "--charset-file",
        help="charset file will be used instead of the arguments specification",
        type=str,
        default="",
    )

    return parser.parse_args()
