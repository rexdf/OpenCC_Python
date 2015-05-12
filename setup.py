from setuptools import setup, Extension

from sys import platform as _platform

if _platform == "darwin":
    # OS X
    link_flags = "-lc++"
elif _platform == "linux" or _platform == "linux2":
    link_flags = "-lstdc++"


setup(
    name="OpenCC",
    author="Rexdf",
    author_email="rexdf@rexdf.org",
    description="OpenCC python wrapper.",
    ext_modules=[
        Extension("_OpenCC", ["OpenCCPython.i"], ["OpenCC/src"],
                  library_dirs=["OpenCC/build/rel/src"],
                  libraries=["opencc"],
                  extra_link_args=[link_flags]),
    ],
)
