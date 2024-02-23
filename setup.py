import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

<<<<<<< HEAD
REPO_NAME = "youtube-trend-forcasting_project"
AUTHOR_USER_NAME = "Harshal"
SRC_REPO = "textSummarizer"
=======
REPO_NAME = "YTrend time series forcasting"
AUTHOR_USER_NAME = "Harshal"
SRC_REPO = "Forcasting"
>>>>>>> 6f1b5977d1e4603902d1fbadcd906344c2c7ac16
AUTHOR_EMAIL = "Harshalhonde50@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
<<<<<<< HEAD
    description="A small python package for forcasting project",
=======
    description="A small python package for NLP app",
>>>>>>> 6f1b5977d1e4603902d1fbadcd906344c2c7ac16
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)