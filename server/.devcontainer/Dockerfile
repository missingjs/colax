FROM python:3.9

ARG USER_NAME
ARG USER_UID
ARG USER_GID

# Create the user
RUN groupadd --gid $USER_GID $USER_NAME \
    && useradd --uid $USER_UID --gid $USER_GID --shell /bin/bash -m $USER_NAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME \
    && chmod 0440 /etc/sudoers.d/$USER_NAME

USER ${USER_NAME}

ENV PATH=/home/vscode/.local/bin:$PATH
ENV COLAX_CONSUL_ADDR=consul-client:8500
