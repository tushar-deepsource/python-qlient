""" This file contains the package setup

:author: Daniel Seifert
:created: 09.09.2021
:copyright: Swisscom
"""
from pathlib import Path

from setuptools import setup

PROJECT_DIR = Path(__file__).resolve().parent

ABOUT_PATH = PROJECT_DIR / "src" / "qlient" / "__about__.py"
README_PATH = PROJECT_DIR / "README.md"
REQUIREMENTS_PATH = PROJECT_DIR / "requirements.txt"
TEST_REQUIREMENTS_PATH = PROJECT_DIR / "requirements" / "test.txt"
DEV_REQUIREMENTS_PATH = PROJECT_DIR / "requirements" / "dev.txt"
DOCS_REQUIREMENTS_PATH = PROJECT_DIR / "requirements" / "docs.txt"


def read_about() -> dict:
    """ Load the qlient/__about__.py globals into the about variable defined below

    :return: the globals from the __about__.py file
    """
    about = {}
    exec(ABOUT_PATH.read_text(encoding="UTF-8"), about)
    return about


def read_requirements_file(req_file_path: Path) -> list:
    """ Read and split the content of a requirements file

    :param req_file_path: holds the path to the requirements file
    :return: a list of strings with the requirements
    """
    content = req_file_path.read_text(encoding="UTF-8")
    return content.splitlines()


ABOUT = read_about()
README = README_PATH.read_text(encoding="UTF-8")
INSTALL_REQUIRES = read_requirements_file(REQUIREMENTS_PATH)
TEST_REQUIRES = read_requirements_file(TEST_REQUIREMENTS_PATH)
DEV_REQUIRES = read_requirements_file(DEV_REQUIREMENTS_PATH)
DOCS_REQUIRES = read_requirements_file(DOCS_REQUIREMENTS_PATH)

PACKAGES = ["qlient"]

setup(
    name=ABOUT["__package_name__"],
    version=ABOUT["__version__"],
    description=ABOUT["__description__"],
    long_description=README,
    long_description_content_type="text/markdown",
    author=ABOUT["__author__"],
    author_email=ABOUT["__author_email__"],
    url=ABOUT["__url__"],
    package_dir={"": "src"},
    packages=PACKAGES,
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    test_requires=TEST_REQUIRES,
    extras_require={
        "test": TEST_REQUIRES,
        "dev": DEV_REQUIRES,
        "docs": DOCS_REQUIRES,
    },
    keywords=ABOUT["__keywords__"],
    license=ABOUT["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    project_urls={
        "Documentation": ABOUT["__url__"],
        "Source": ABOUT["__source__"],
    },
)
