from python:3.11.1-buster

WORKDIR /

RUN pip install runpod

ADD src/handler.py .

CMD [ "python", "-u", "/handler.py" ]
