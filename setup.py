import setuptools
<<<<<<< HEAD

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
=======
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"
>>>>>>> 74c640564df2d27a4e14ce5b6327800cbbfd9aef

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "AHMEDAlAA-A3"
SRC_REPO = "textSummarizer"
<<<<<<< HEAD
AUTHOR_EMAIL = "a7med3laa3333@gmail.com"
=======
AUTHOR_EMAIL = "medo.oreif@gmail.com"

>>>>>>> 74c640564df2d27a4e14ce5b6327800cbbfd9aef

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
<<<<<<< HEAD
    long_description_content_type="text/markdown",
=======
    long_description_content="text/markdown",
>>>>>>> 74c640564df2d27a4e14ce5b6327800cbbfd9aef
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)