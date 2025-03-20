from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    description="A brief description of your project",
    author="Mohsin Kirmani",
    packages=find_packages(),
    install_requires=[
        "requests==2.28.2",
        "numpy==1.24.2",
        "pandas==1.5.3",
        "matplotlib==3.7.1",
        "scikit-learn==1.2.0",
        "flask==2.2.3",
    ],
)
