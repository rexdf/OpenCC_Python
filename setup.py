from setuptools import setup, Extension
from sys import maxsize as _maxsize

is_64bits = _maxsize > 2**32
arch = 64 if is_64bits else 32

setup(
    name="OpenCC",
    author="Rexdf",
    author_email="rexdf@rexdf.org",
    description="OpenCC python wrapper.",
    ext_modules=[
        Extension("_OpenCC", ["OpenCCPython.i"], ["OpenCC/src"],
                  library_dirs=["OpenCC/OpenCC_%d/src/Release/" % arch],
                  libraries=["opencc"]),
    ],
)
