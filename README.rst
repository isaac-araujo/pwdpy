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

    $ pwdpy {generate, entropy, strengthen} [-h]
    
    $ pwdpy generate [-h] [-l LENGTH] [-q QUANTITY] [-p] [-d] [-le] [-nu] [-nl] [-cf FILE] [-o FILE]
    
    $ pwdpy entropy [-h] [-pwd PASSWORD]
    
    $ pwdpy strengthen [-h] [-pwd PASSWORD] [-shf] [-inc] [-mp MAX_PREFIX] [-ms MAX_SUFIX]

Commands:
    **generate**      Generates a random password based on the arguments
    
    **entropy**       Calculate the entropy of a password
    
    **strengthen**    Strengthen your password

ALL Arguments:

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

STRENGTHEN Arguments:

-pwd, --password PASSWORD 
    password that will be strengthened
    
-shf, --shuffle
    shuffle the password after strengthened (default: False)
    
-inc, --increase
    increase the number of characters in the password (default: False)
    
-mp, --max_prefix MAX_PREFIX
    max number of characters to add as prefix (default: 5) can only be used with --increase
    
-ms, --max_sufix MAX_SUFIX
    max number of characters to add as sufix (default: 5) can only be used with --increase

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
    
    $ pwdpy entropy -pwd "Isaac"
        28.5

Python module
=============

pwdpy Python module provides one function that is called generate.

| ``generate(quantity=1, length=12, punctuation=True, digits=True, letters=True, l_upper=True, l_lower=True, charset=[], charset_file="", **kwargs)``

    It returns a string with *length* characters. *punctuation*, *digits*
    and *letters* arguments specify whether punctuation, digits and letters
    should be used. *l_upper* and *l_lower* specifies letter wich case the letter can be.
    
    A list of charsets can be passed, instead of using the default it will uses the parameter.
    
    You can configure an output using *charset_file*, that file will be
    created or replaced with the generated passwords
    
    
| ``entropy(password: str) -> float``

    It returns a float of bits that was the result of applying the Shannon formula.

| ``strengthen(password: str, shuffle=False, increase=True, max_prefix=5, max_sufix=5) -> str``

    It returns a string the strengthen password,
    can be added a prefix and/or sufix by using *max_prefix* and *max_sufix*
    and the password can be shuffle using *shuffle*.


License
--------
MIT License
