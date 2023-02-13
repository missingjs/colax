#!/bin/bash

usage()
{
    cat << EOF
usage: colax project <command> [options]

Commands:
    create <name>    Create new project with given name.
EOF
    exit 1
}

cmd=$1

[ -z $cmd ] && usage

function create_project()
{
    local prj_name=$1
    local prj_file="colax.proj.conf"
    [ -e $prj_file ] && { echo "Error: $prj_file already exist"; exit 3; }
    cat >$prj_file <<EOF
project_name = $prj_name
EOF

    cat >colax-test.json <<EOF
{
    "tests": [
        {
            "args": [1, 2],
            "result": 3
        }
    ]
}
EOF

    echo "Project $prj_name created"
}

case $cmd in
    create)
        proj_name=$2
        [ -z $proj_name ] && usage
        create_project $proj_name
        ;;
    *)
        usage
        ;;
esac
