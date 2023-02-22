from setuptools import setup, find_packages

VERSION = "0.2.1"
DESCRIPTION = "Password Tools"

with open('README.rst') as file:
    long_description = file.read()

# Setting up
setup(
    name="pwdpy",
    version=VERSION,
    author="Isaac Araujo",
    author_email="<zac.araujo2001@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "password", "password generator", "password tools"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
