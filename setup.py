from pathlib import Path
from setuptools import setup, find_namespace_packages

BASE_DIR = Path(__file__).parent

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

test_packages = [
    "coverage[toml]==6.0.2",
    "great-expectations",
    "pytest==6.0.2",
    "pytest-cov==2.10.1",
]

dev_packages = [
    "black==20.8b1",
    "flake8==3.8.3",
    "isort==5.5.3",
    "jupyterlab==2.2.8",
    "pre-commit==2.11.1",
]

setup(name="dk",
    license = "MIT",
    description = "test",
    author = "Daisuke Kuwabara",
    packages=find_namespace_packages(),
    install_requires = [required_packages],
    extras_require={
    "test": test_packages,
    #"dev": #test_packages + dev_packages + docs_packages,
    #"docs": #docs_packages,
},
    entry_points = {
        "console_scripts": [
            "babushuka = babushka.main:app",
        ],
    },
    )
