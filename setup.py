from setuptools import setup, find_packages

setup(
    name='snapshot',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.main:output",
        ],
    },
    author='Yaroslav Kurapov'
)
