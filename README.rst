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

    $ pwdpy generate_wordlist [-h] [-q QUANTITY] [-l LENGTH] [-lg LANGUAGE] [-sep SEP] [-u] [-wl WORDLIST]

Commands:
    **generate**      Generates a random password based on the arguments
    
    **entropy**       Calculate the entropy of a password
    
    **strengthen**    Strengthen your password

    **generate_wordlist**    Generates a random wordlist

ALL Arguments:

-h, --help
    Display help message

-l, --length LENGTH
    The length of the password (default: 8)

-q, --quantity QUANTITY
    Generate QUANTITY passwords. (default: 1)

-sc, --special_characters
    Use special characters (default: False)

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

GENERATE WORDLIST Arguments:

-q QUANTITY, --quantity QUANTITY
    quantity of passwords to generate (default: 1)
                    
-l LENGTH, --length LENGTH
        the length of the password (default: 8)

-lg LANGUAGE, --language LANGUAGE
    language of the words (default: english)

-sep SEP, --separator SEP
    word separation (default: space)

-u, --upper           
    use upper case words (default: False)

-wl WORDLIST, --wordlist WORDLIST
    path to to the wordlist file (default: None)

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
        
STRENGTHEN:
-------
Strengthen one password:

    $ pwdpy strengthen -pwd "Isaac"
        15Á4C
    
    $ pwdpy strengthen -pwd "Isaac" -inc
        <uQ0@îsá4c~
        
Strengthened and using shuffle

    $ pwdpy strengthen -pwd "Python" -shf
        ý%IÕqN

GENERATE WORDLIST:
-------
Generate one wordlist with 13 words:

    $ pwdpy generate_wordlist -l 13
        dollhood obligatum weirded triangularly meanness uncrediting ologies pomological refixture accessible clapperclaws winzeman montesinos

Generate one wordlist with portuguese upper words:

    $ generate_wordlist -lg portuguese -u
        ANDRÔMEDA CUCURBITÁCEO ISOAMÍLICO APLACÁVEL ARQUEÔMETRO GERVAIS CRUSTACÍTICO EUGLIPTO
        
Python module
=============

pwdpy Python module provides one function that is called generate.

| ``generate(quantity=1, length=12, special_characters=True, digits=True, letters=True, l_upper=True, l_lower=True, charset=[], charset_file="",output_file="", **kwargs) -> str or list``

    It returns a string with *length* characters. *special_characters*, *digits*
    and *letters* arguments specify whether special characters, digits and letters
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

| ``generate_wordlist(quantity=1, length=8, language="english", sep=" ", case="lower", wordlist: str = None) -> str orlist``
    
    It returns a string with *length* of words.
    The words are select by *language* and separeted by *sep*.
    Define case of the words using *case*.
    Or you can pass your own wordlist using *wordlist*.

License
--------
MIT License
