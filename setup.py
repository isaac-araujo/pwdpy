from setuptools import setup, find_packages

VERSION = "0.5.0"
DESCRIPTION = "Password Tools"

with open("README.rst", encoding="utf-8") as file:
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
    # url="https://github.com/isaac-araujo/pwdpy",
    project_urls={
        "Source": "https://github.com/isaac-araujo/pwdpy",
    },
    license="MIT License",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["pwdpy = pwdpy.pwdpy:main"]},
    keywords=["python", "password", "password generator", "password tools"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    # python_requires = ">=3.7",
)
