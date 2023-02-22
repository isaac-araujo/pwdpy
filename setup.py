from setuptools import setup, find_packages

VERSION = "0.2.0"
DESCRIPTION = "Password Tools"
LONG_DESCRIPTION = "pwdpy is a set of tools to facilitate password handling."

# Setting up
setup(
    name="pwdpy",
    version=VERSION,
    author="Isaac Araujo",
    author_email="<zac.araujo2001@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
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
