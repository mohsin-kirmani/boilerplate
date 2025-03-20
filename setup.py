from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    description="A brief description of your project",
    author="Mohsin Kirmani",
    packages=find_packages(),
    install_requires=[
        "requests",
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "flask",
    ],
)
