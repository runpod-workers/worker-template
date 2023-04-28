from python:3.11.1-buster

WORKDIR /

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    rm /requirements.txt

ADD src .

CMD [ "python", "-u", "/handler.py" ]
