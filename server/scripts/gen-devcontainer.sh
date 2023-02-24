#!/bin/bash

self_dir=$(cd $(dirname $0) && pwd)
proj_dir=$(realpath $self_dir/..)

cd $proj_dir

container_user=vscode
user_uid=$(id -u)
user_gid=$(id -g)

cat >.devcontainer/devcontainer.json << EOF
// For format details, see https://aka.ms/devcontainer.json. For config options, see the README at:
// https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3
{
    "name": "colax-server",
    "build": {
        "dockerfile": "Dockerfile",
        "context": "..",
        "args": {
            // Update 'VARIANT' to pick a Python version: 3, 3.10, 3.9, 3.8, 3.7, 3.6
            // Append -bullseye or -buster to pin to an OS version.
            // Use -bullseye variants on local on arm64/Apple Silicon.
            "USER_NAME": "$container_user",
            "USER_UID": "$user_uid",
            "USER_GID": "$user_gid"
        }
    },

    // Configure tool-specific properties.
    "customizations": {
        // Configure properties specific to VS Code.
        "vscode": {
            // Set *default* container specific settings.json values on container create.
            "settings": {
                // "python.analysis.typeCheckingMode": "basic",
                "python.defaultInterpreterPath": "/usr/local/bin/python",
                "python.linting.enabled": true,
                "python.linting.pylintEnabled": true,
                "python.formatting.autopep8Path": "/usr/local/py-utils/bin/autopep8",
                "python.formatting.blackPath": "/usr/local/py-utils/bin/black",
                "python.formatting.yapfPath": "/usr/local/py-utils/bin/yapf",
                "python.linting.banditPath": "/usr/local/py-utils/bin/bandit",
                "python.linting.flake8Path": "/usr/local/py-utils/bin/flake8",
                "python.linting.mypyPath": "/usr/local/py-utils/bin/mypy",
                "python.linting.pycodestylePath": "/usr/local/py-utils/bin/pycodestyle",
                "python.linting.pydocstylePath": "/usr/local/py-utils/bin/pydocstyle",
                "python.linting.pylintPath": "/usr/local/py-utils/bin/pylint"
            },

            // Add the IDs of extensions you want installed when the container is created.
            "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance"
            ]
        }
    },

    // Use 'forwardPorts' to make a list of ports inside the container available locally.
    // "forwardPorts": [],

    // Use 'postCreateCommand' to run commands after the container is created.
    "postCreateCommand": "/bin/bash scripts/install-dev-tools.sh",

    // Comment out to connect as root instead. More info: https://aka.ms/vscode-remote/containers/non-root.
    "remoteUser": "$container_user",

    "runArgs": ["--network", "colax-server"],

    "appPort": ["6733:8000"]
}
EOF

echo "$proj_dir/.devcontainer/devcontainer.json"
