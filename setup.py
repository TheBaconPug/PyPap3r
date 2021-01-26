import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyPaper", # Replace with your own username
    version="0.0.1",
    author="TheBaconPug",
    description="A python package that can change your mac's desktop background to a file or a url",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.thebaconpug.com/pipaper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)