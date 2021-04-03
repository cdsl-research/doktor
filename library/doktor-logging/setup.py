import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="doktor_logging",
    version="0.1.0",
    author="Tomoyuki KOYAMA",
    author_email="tomoyuki@koyama.me",
    description="Logging Library for doktor.",
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
    python_requires='>=3.8',
)
