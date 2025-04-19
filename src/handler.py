"""Example handler file."""

import runpod

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.


def handler(job):
    """Handler function that will be used to process jobs."""
    job_input = job["input"]

    name = job_input.get("name", "World")

    return f"Hello, {name}!"


runpod.serverless.start({"handler": handler})
