import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="helloworld-hariprasath6112001",
    version="1.3",
    author="HariPrasath.S.S",
    author_email="hariprasath6112001@gmail.com",
    scripts=["helloworld"],
    description="Print Hello World",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hairprasath6112001/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
