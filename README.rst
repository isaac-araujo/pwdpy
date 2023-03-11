pwdpy
=======

pwdpy is a set of tools to facilitate password handling. It can be used in command line and as a python module.

Installation
============

pwdpy requires Python 3.x.

pwdpy can be installed with *pip*:

    $ pip install pwdpy

Usage (command line)
====================

pwdpy accepts several arguments configuring its outcome.
Overall synopsis is:

    $ pwdpy {generate, entropy} [-h] [-l LENGTH] [-q QUANTITY] [-p] [-d] [-le] [-nu] [-nl] [-cf FILE] [-o FILE]

Commands:
    **generate**      Generates a random password based on the arguments
    
    **entropy**       Calculate the entropy of a password

GENERATE Arguments:

-h, --help
    Display help message

-l, --length LENGTH
    The length of the password (default: 8)

-q, --quantity QUANTITY
    Generate QUANTITY passwords. (default: 1)

-p, --punctuation
    Use punctuation characters (default: False)

-d, --digits
    Use digits (default: False)

-le, --letters
    Use letter (default: False)

-nu, --no-upper
    Don't use upper case letters (default: False)

-nl, --no-lower
    Don't use lower case letters (default: False)

-cf, --charset-file FILE
    Charset file will be used instead of the arguments specification
    
-o FILE, --output FILE
    The output file will be created with the passwords.

ENTROPY Arguments:

-pwd, --password PASSWORD 
    password that will be tested

Examples
--------

Below are some examples of pwdpy usage.

GENERATE:
-------
One password with letters and digits:

    $ pwdpy generate -le -d 
        MT06aRK1

One password with 12 digits:

    $ pwdpy generate -l 12 -d
        304751766483

One password with all characters possibility:

    $ pwdpy generate -le -d -p
        PY>8OH+y

A list containing 3 passwords with all characters possibility:

    $ pwdpy generate -q 3 -le -d -p
        ['Xw]6ua77', 'SfmCrlg)', 'I9):o8Oa']

One password with all characters possibility from the charset file:

    $ pwdpy generate -cf ./wordlist.txt
        }=W8jb4y

ENTROPY:
-------
Calculing one password entropy:

    $ pwdpy entropy -pwd "PY>8OH+y"
        52.44

Python module
=============

pwdpy Python module provides one function that is called generate.

| ``def generate(quantity=1, length=8, punctuation=True, digits=True, letters=True, l_upper=True, l_lower=True, charset=[], charset_file="", **kwargs)``

It returns a string with *length* characters. *punctuation*, *digits*
and *letters* arguments specify whether punctuation, digits and letters
should be used. *l_upper* and *l_lower* specifies letter wich case the letter can be.


License
--------
MIT License
