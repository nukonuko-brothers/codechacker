from setuptools import setup, find_packages

setup(
    name="code_checker",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "code_checker=code_checker.checker:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python code checker for PEP 8 compliance",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/code_checker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
