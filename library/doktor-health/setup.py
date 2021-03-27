import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="doktor_health",
    version="0.1.0",
    author="Takamasa Iijima",
    author_email="takahyon@gmail.com",
    description="This library is used to monitor the state of the doktor microservice, a thesis search service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cdsl-research/doktor-health",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={},
    python_requires='>=3.7',
)
