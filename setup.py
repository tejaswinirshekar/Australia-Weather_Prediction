from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Australia_Weather_Prediction",
    version="0.1",
    author="Tejaswini",
    packages=find_packages(),
    install_requires = requirements,
)