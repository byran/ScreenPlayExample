#!/bin/bash

readonly SCRIPT_PATH=$(realpath $(dirname $0))
cd "$SCRIPT_PATH"

source .venv/bin/activate

cd docs/test_results
screenplay2sphinx-all

cd ..

make clean
make html
