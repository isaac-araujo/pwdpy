from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'Password Tools'
LONG_DESCRIPTION = 'A package that allows to generate simple to complex passwords'

# Setting up
setup(
    name="pwdpy",
    version=VERSION,
    author="Isaac Araujo",
    author_email="<mail@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['random'],
    keywords=['python', 'password', 'password generator', 'password tools'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)