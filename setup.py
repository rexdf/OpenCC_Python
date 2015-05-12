from setuptools import setup, Extension


setup(
    name="OpenCC",
    author="Rexdf",
    author_email="rexdf@rexdf.org",
    description="OpenCC python wrapper.",
    ext_modules=[
        Extension("_OpenCC", ["OpenCCPython.i"], ["OpenCC/src"],
                  library_dirs=["OpenCC/build/rel/src"],
                  libraries=["opencc"]),
    ],
)
