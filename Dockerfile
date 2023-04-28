FROM BASE_IMAGE=runpod/pytorch:3.10-2.0.0-117

WORKDIR /

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    rm /requirements.txt

ADD src .

CMD [ "python", "-u", "/handler.py" ]
