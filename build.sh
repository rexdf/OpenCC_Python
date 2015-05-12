#!/bin/env sh

set -e
set -x

pushd OpenCC
make
popd

python setup.py build

mkdir out

cp build/*/*.so out/
cp OpenCC/build/rel/data/*.ocd out/
cp OpenCC/build/rel/data/*.txt out/
cp OpenCC/data/config/*.json out/