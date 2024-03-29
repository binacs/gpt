FROM python:slim-buster

COPY . /src

RUN pip3 install -r /src/requirements.txt

CMD python3 /src/main.py