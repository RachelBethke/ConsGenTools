from setuptools import setup, find_packages

setup(
    name="genetics",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "tk",
    ],
)