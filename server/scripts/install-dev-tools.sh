#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)
proj_dir=$(realpath $self_dir/..)

cd $proj_dir || exit

set -xe

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

sudo apt-get install -y tig tree vim iputils-ping net-tools
