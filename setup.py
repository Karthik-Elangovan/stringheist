from setuptools import setup, find_packages

setup(
    name="stringheist",
    version="0.1.0",
    description="String template rendering library",
    author="Karthik Elangovan",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
