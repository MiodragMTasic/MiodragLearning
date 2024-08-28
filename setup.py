from setuptools import setup, find_packages

setup(
    name="probability_theory_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "sympy",
        "pandas",
    ],
    author="Miodrag Tasic",
    author_email="miodragmtasic@gmail.com",
    description="A library for probability theory and information theory calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/miodragmtasic/probability_theory_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
