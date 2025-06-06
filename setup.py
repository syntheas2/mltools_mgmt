from setuptools import setup, find_packages
import os

# Read README if it exists, otherwise use description
descr = "syntheas_mltools_mgmt"
long_description = descr
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="syntheas_mltools_mgmt",
    version="0.1.0",
    packages=find_packages(include=['syntheas_mltools_mgmt']),
    install_requires=[],
    author="virsel",
    author_email="your.email@example.com",
    description=descr,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11,<3.12",
)