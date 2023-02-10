#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)

usage()
{
    cat << EOF
usage: colax worker python [<operation>] [args]...

Operations:

    start     Start worker.

    stop      Stop worker.

    status    Show status.
EOF
    exit 1
}

operation=$1

[ -z $operation ] && usage

function prepare_volumes()
{
    local top_dir="$HOME/.colax/volumes/worker/python/problems"
    [ -e $top_dir ] || mkdir -p $top_dir || exit
}

cd $self_dir

case $operation in
    start)
        prepare_volumes
        docker compose up -d
        ;;
    stop)
        docker compose down -t 5
        ;;
    status)
        docker compose ps
        ;;
    *)
        usage
        ;;
esac
