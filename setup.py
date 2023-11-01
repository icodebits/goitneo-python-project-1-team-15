from setuptools import setup, find_namespace_packages

setup(
    name="cli-bot",
    description="Python-cli personal assistant",
    url="https://github.com/icodebits/goitneo-python-project-1-team-15",
    version="0.0.1",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["Click"],
)
