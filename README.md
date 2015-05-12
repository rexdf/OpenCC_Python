# OpenCC_Python
OpenCC Python Extension with no external dependencies for Linux OSX and Windows

First of all check the python version you want. like: 64bit or 32bit, 2.7.9 or 3.3.3 or 3.4.2. Use python -version to check. Make sure that the python version you need is current aviable from path.

##Clone the repo

    cd ~
    git clone https://github.com/rexdf/OpenCC_Python.git
    cd OpenCC_Python
    git submodule init
    git submodule update

##Build

    sh ./build.sh

##Test
Now you can run some test.

    cd ~/OpenCC_Python
    python test.py

For Windows build, Please refer [here](https://github.com/rexdf/OpenCC_Python/blob/windows/README.md).