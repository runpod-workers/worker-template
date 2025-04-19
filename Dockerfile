FROM runpod/base:0.6.2-cuda11.8.0

# Install dependencies
COPY requirements.txt /requirements.txt
RUN uv pip install --upgrade -r /requirements.txt --no-cache-dir

# Add src files
ADD src .

# Run the handler
CMD python3.11 -u /handler.py
