import sys
# Available at setup time due to pyproject.toml
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext,ParallelCompile
from setuptools import setup

__version__ = "0.0.1"


ext_modules = [
    Pybind11Extension("PokerPy",
        ["src/main.cpp"],
        cxx_std=20
        ),
]

setup(
    name="PokerPy",
    version=__version__,
    author="Gonzalo Lope",
    author_email="gonzalolopecc@gmail.com",
    url="https://github.com/glpcc/Poker_probs",
    description="A fast poker probabilities calculator.",
    long_description="",
    ext_modules=ext_modules,
    install_requires=[
        'pybind11'
    ],
    package_data={
        "PokerPy":["types.pyi","__init__.pyi"],
    },
    packages=["PokerPy"],
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    # cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)