#!/bin/sh

pip3 -V
pip3 install --target="./local_lib" --upgrade --ignore-installed git+https://github.com/jaraco/path.git --log intsall_python_py.log
python3 ./my_program.py