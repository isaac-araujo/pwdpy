import argparse


class ArgParser:
    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(
            prog="pwdpy", description="Tools for passwords"
        )
        subparser = parser.add_subparsers(
            title="commands", help="list of tools that can be used", dest="command"
        )

        # GENERATE
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
            "-sc",
            "--special_characters",
            help="use special characters (default: False)",
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
            "-nle",
            "--no-letters",
            help="don't use letters (default: True)",
            action="store_false",
            default=True,
            dest="letters"
        )

        generate.add_argument(
            "-nu",
            "--no-upper",
            help="don't use upper case letters (default: True)",
            action="store_false",
            default=True,
            dest="upper",
        )

        generate.add_argument(
            "-nl",
            "--no-lower",
            help="don't use lower case letters (default: True)",
            action="store_false",
            default=True,
            dest="lower",
        )

        generate.add_argument(
            "-cf",
            "--charset-file",
            metavar="FILE",
            help="charset file will be used instead of the arguments specification",
            type=str,
            default="",
        )

        generate.add_argument(
            "-o",
            "--output",
            metavar="FILE",
            help="The output file will be created with the passwords.",
            type=str,
            default="",
        )

        # ENTROPY
        entropy = subparser.add_parser(
            "entropy", help="calculate the entropy of the password"
        )

        entropy.add_argument(
            "-pwd",
            "--password",
            help="password that will be tested",
            type=str,
            required=True,
            dest="password",
        )

        # STRENGTHEN
        strengthen = subparser.add_parser("strengthen", help="strengthen your password")

        strengthen.add_argument(
            "-pwd",
            "--password",
            help="password that will be strengthened",
            type=str,
            required=True,
            dest="password",
        )

        strengthen.add_argument(
            "-shf",
            "--shuffle",
            help="shuffle the password after strengthened (default: False)",
            action="store_true",
            default=False,
        )

        strengthen.add_argument(
            "-inc",
            "--increase",
            help="increase the number of characters in the password (default: False)",
            action="store_true",
            default=False,
        )

        strengthen.add_argument(
            "-mp",
            "--max_prefix",
            help=(
                "max number of characters to add as prefix (default: 5) can only be used with --increase"
            ),
            type=int,
            default=5,
        )

        strengthen.add_argument(
            "-ms",
            "--max_sufix",
            help=(
                "max number of characters to add as sufix (default: 5) can only be used with --increase"
            ),
            type=int,
            default=5,
        )

        generate_wordlist = subparser.add_parser(
            "generate_wordlist", help="generates wordlist based on the arguments"
        )

        generate_wordlist.add_argument(
            "-q",
            "--quantity",
            help=(
                "quantity of passwords to generate (default: 1)"
            ),
            type=int,
            default=1,
        )
        
        generate_wordlist.add_argument(
            "-l",
            "--length",
            help="the length of the password (default: 8)",
            type=int,
            default=8,
        )

        generate_wordlist.add_argument(
            "-lg",
            "--language",
            help="language of the words (default: english)",
            type=str,
            default="english",
        )

        generate_wordlist.add_argument(
            "-sep",
            "--separator",
            help="word separation (default: space)",
            type=str,
            default=" ",
            dest="sep",
        )

        generate_wordlist.add_argument(
            "-u",
            "--upper",
            help="use upper case words (default: False)",
            action="store_const",
            const="upper",
            default="lower",
            dest="case",
        )

        generate_wordlist.add_argument(
            "-wl",
            "--wordlist",
            help="path to to the wordlist file (default: None)",
            default=None,
        )

        return parser.parse_args()
