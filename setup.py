from setuptools import setup

setup(
    name="Birk",
    version="1.0",
    author="Melano",
    url="https://github.com/1b0325h/Birk",
    license="MIT",
    py_modules=["birk"],
    install_requires=[
        "colorama==0.4.3",
        "fire==0.4.0",
        "tqdm==4.43.0",
        "PyYAML==5.3.1"],
    entry_points={"console_scripts": ["birk = birk:main"]})
