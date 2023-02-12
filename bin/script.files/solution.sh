#!/bin/bash

usage()
{
    cat <<EOF
usage: colax solu <command> <lang> [options]

Commands:
    new    create solution in specific language
    run    submit solution
EOF
    exit 1
}

cmd=$1
language=$2
[ -z $language ] && usage
entry=$COLAX_HOME/worker/$language/bin/solu.sh
[ -e $entry ] || { echo "Error: language $language not supported"; exit 5; }

case $cmd in
    new)
        filename=$(bash $entry filename)
        [ -e $filename ] && { echo "Error: $filename already exist"; exit 4; }
        bash $entry template > $filename || exit
        echo "$filename OK"
        ;;
    run)
        filename=$(bash $entry filename)
        python3 $COLAX_HOME/bin/script.files/submit.py $language $filename
        ;;
    *)
        usage
        ;;
esac
