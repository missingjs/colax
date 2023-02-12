#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)
sdk_dir=$(realpath $self_dir/..)

usage()
{
    cat <<EOF
usage: colax solu python <command> [options]

Commands:
    filename   Display name of source file.
    template   Display template content
EOF
    exit 1
}

cmd=$1

[ -z $cmd ] && usage

case $cmd in
    filename)
        echo "solution.py"
        ;;
    template)
        cat $sdk_dir/template.py
        ;;
        # src_file=solution.py
        # [ -e $src_file ] && { echo "Error: $src_file already exist"; exit 4; }
        # cp $tmpl_file $src_file || exit
        # echo "$src_file OK"
    *)
        ;;
esac
