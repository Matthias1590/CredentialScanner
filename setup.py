from setuptools import setup


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="credentialscanner",
    version="1.0.0",
    description="A python module to make sure that no sensitive information gets published when commiting to git.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matthias1590/CredentialScanner",
    author="Matthias Wijnsma",
    author_email="matthiasx95@gmail.com",
    license="MIT",
    packages=["credentialscanner"]
)