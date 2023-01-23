import sys
# Available at setup time due to pyproject.toml
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"


ext_modules = [
    Pybind11Extension("poker_probs",
        ["src/main.cpp"],
        ),
]

setup(
    name="poker_probs",
    version=__version__,
    author="Gonzalo Lope",
    author_email="gonzalolopecc@gmail.com",
    url="https://github.com/glpcc/Poker_probs",
    description="A fast poker probabilities calculator.",
    long_description="",
    ext_modules=ext_modules,
    # packages=["poker_probs", "unohelper"],
    package_data={
        "poker_probs":["py.typed","__init__.pyi"],
    },
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)