FROM python:3.9

WORKDIR /root

COPY . /root

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
    && chmod 755 run.sh

CMD /bin/bash run.sh
