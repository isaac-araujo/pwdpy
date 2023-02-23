import argparse

# commands option
GENERATE = ["generate"]
TEST = ["test"]


def get_args():
    parser = argparse.ArgumentParser(prog="pwdpy", description="Tools for passwords")
    subparser = parser.add_subparsers(
        title="commands", help="list of tools that can be used", dest="command"
    )

    generate = subparser.add_parser(
        "generate", help="generates a random password based on the arguments"
    )

    generate.add_argument(
        "-l",
        "--length",
        help="the length of the password (default: 8)",
        type=int,
        default=8,
    )

    generate.add_argument(
        "-q",
        "--quantity",
        help="quantity of passwords to generate (default: 1)",
        type=int,
        default=1,
    )

    generate.add_argument(
        "-p",
        "--punctuation",
        help="use punctuation characters (default: False)",
        action="store_true",
        default=False,
    )

    generate.add_argument(
        "-d",
        "--digits",
        help="use digits (default: False)",
        action="store_true",
        default=False,
    )

    generate.add_argument(
        "-le",
        "--letters",
        help="use letter (default: False)",
        action="store_true",
        default=False,
    )

    generate.add_argument(
        "-nu",
        "--no-upper",
        help="don't use upper case letters (default: False)",
        action="store_false",
        default=True,
        dest="upper",
    )

    generate.add_argument(
        "-nl",
        "--no-lower",
        help="don't use lower case letters (default: False)",
        action="store_false",
        default=True,
        dest="lower",
    )

    generate.add_argument(
        "-cf",
        "--charset-file",
        help="charset file will be used instead of the arguments specification",
        type=str,
        default="",
    )

    test = subparser.add_parser("test", help="test the strength of the password")

    test.add_argument(
        "-pwd",
        "--password",
        help="password that will be tested",
        type=str,
        required=True,
        dest="password",
    )

    return parser.parse_args()
