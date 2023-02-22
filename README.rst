pwdpy
=======

pwdpy is a set of tools to facilitate password handling. It can be used in command line and as a python module.

Installation
============

pwdpy requires Python 3.x.

pwdpy can be installed with *pip*::

    $ pip install pwdpy

To install it from source, enter the source distribution directory and run::

    $ python setup.py install

Usage (command line)
====================

The most basic usage of pwdpy command line utility prints 10 random
passwords, and is as follows::

    $ pwdpy

pwdpy accepts several arguments configuring its outcome.
Overall synopsis is::

    $ pwdpy [-h] [-l LENGTH] [-q QUANTITY]
            [-p] [-d] [-le] [-nu] [-nl]

Arguments:

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

Examples
--------

Below are some examples of pwdpy usage.

Output: one password with letters and digits::

    $ pwdpy -le -d 
    MT06aRK1

Output one password with 12 digits::

    $ pwdpy -l 12 -d
    304751766483

Output one password with all characters possibility::

    $ pwdpy -le -d -p
    PY>8OH+y

Output: a list containing 3 passwords with all characters possibility::

    $ pwdpy -q 3 -le -d -p
    ['Xw]6ua77', 'SfmCrlg)', 'I9):o8Oa']

Python module
=============

pwdpy Python module provides one function that is called generate.

| ``def generate( quantity=1, length=8, punctuation=True, digits=True, letters=True, l_upper=True, l_lower=True, charset="", **kwargs ):``

It returns a string with *length* characters. *punctuation*, *digits*
and *letters* arguments specify whether punctuation, digits and letters
should be used. *l_upper* and *l_lower* specifies letter wich case the letter can be.


License
--------
MIT
