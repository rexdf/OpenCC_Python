# OpenCC_Python
OpenCC Python Extension with no external dependencies for Linux OSX and Windows

This readme is for Visual studio 2013 or higher. And you need to install [cmake](http://www.cmake.org).

First of all check the python version you want. like: 64bit or 32bit, 2.7.9 or 3.3.3 or 3.4.2. Use `python -version` to check. Make sure that the python version you need is current aviable from path.

##Clone the repo

    git clone -b windows https://github.com/rexdf/OpenCC_Python.git
    cd OpenCC_Python
    git submodule init
    git submodule update

##Build

### build a OpenCC static library
- go to `OpenCC_Python\OpenCC`, run `__run_cmake x64.bat` or `__run_cmake x86.bat` (or both).

- If everything goes well, you find one or two more folders `OpenCC_32` and `OpenCC_64`.

-  Open `_OpenCC.sln` in the above folder with Visual studio 2013 or higher. Change to Release and build. Close it now.

### build opencc python extension
- Now you need open `VS2013 x86 Native Tools Command Prompt` or `VS2013 x64 Native Tools Command Prompt` or `VS2013 x64 Cross Tools Command Prompt` from your start menu(or metro/modern UI).
- run `path=D:\python33_64;%path%` to add python you need to your path.
- run `set DISTUTILS_USE_SDK=1` and `set MSSdk=1`
- now cd to `OpenCC_Python` folder.
- python setup.py build

### copy files
- Copy `_OpenCC.pyd` from `OpenCC_Python\build\lib.win-amd64-3.3` to `OpenCC_Python\out	`. (You need to build a out in `OpenCC_Python`.
- copy all json files from `OpenCC_Python\OpenCC\data\config` to `OpenCC_Python\out`.
- copy **correct arch(32 or 64) ocd** from `OpenCC_Python\OpenCC\OpenCC_32\data` or `OpenCC_Python\OpenCC\OpenCC_64\data` to `OpenCC_Python\out`.

##Test
Now you can run some test.(copy files is required before Test)

    cd OpenCC_Python
    python test.py

For Linux or OSX build, Please refer [here](https://github.com/rexdf/OpenCC_Python/blob/master/README.md).