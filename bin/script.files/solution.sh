#!/bin/bash

usage()
{
    cat <<EOF
usage: colax solu <command> [options]

Commands:
    new <lang>    create solution in specific language
    run <lang>    submit solution
EOF
    exit 1
}

cmd=$1

case $cmd in
    new)
        language=$2
        [ -z $language ] && usage
        entry=${COLAX_HOME}/worker/$language/bin/solu.sh
        [ -e $entry ] || { echo "language $language not supported"; exit 5; }
        bash $entry create
        ;;
    run)
        ;;
    *)
        usage
        ;;
esac
