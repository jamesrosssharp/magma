import numpy as np
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="mag_parser",
    ext_modules=cythonize(["src/MagParser.pyx", "src/MagDatabase.pyx"], compiler_directives={'language_level': "3"}),
    include_dirs=[np.get_include(), "src"]
)
