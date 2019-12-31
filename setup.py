import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="threefive", 
    version="2.0.07",
    author="fu-corp",
    author_email="spam@futzu.com",
    description="SCTE 35 Parser/Decoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/threefive",
    packages=setuptools.find_packages(),
    install_requires=['bitslicer9k',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
