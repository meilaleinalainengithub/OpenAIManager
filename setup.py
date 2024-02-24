from setuptools import setup, find_packages

with open("README.md", "r") as f:
    desc = f.read()

setup(name="mllopenaimanager",
    version='0.2.2',
    packages=find_packages(),
    install_requires=['openai>=1.12.0'],
    long_description=desc,
    long_description_content_type="text/markdown"
)