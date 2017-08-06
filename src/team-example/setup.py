from setuptools import setup, find_packages

setup(
    name="team-example",
    version="0.1",
    packages=find_packages(exclude=['test', 'test*', 'test.*', '*.test', '*.test.*']),
)
