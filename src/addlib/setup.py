from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

name = "addlib_py"

ext_modules = Extension(
    name=name,
    sources=["addlib.pyx"],
    language="c++",
    libraries=["addlib"],
    library_dirs=["."],
    include_dirs=["."]
)
setup(
    name=name,
    ext_modules=cythonize([ext_modules])
)