from setuptools import setup, find_packages

with open(file='README.md', mode='r', encoding='utf-8') as file:
    long_description = file.read()

__version__ = '0.0.1'

REPO_NAME = 'twoFace-match-Deepface'
AUTHOR_USER_NAME = 'GyanPrakashkushwaha'
SRC_REPO = 'src'
AUTHOR_EMAIL = 'gyanp7880@gmail.com'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Identifies similarity between two faces',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=find_packages(where=SRC_REPO),
    package_dir={SRC_REPO: SRC_REPO},
    long_description=long_description,
)





