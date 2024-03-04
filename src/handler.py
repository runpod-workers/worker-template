""" Example handler file. """

import os
import runpod
import dotenv
import urllib.request
import demucs.separate

dotenv.load_dotenv()
# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.

def handler(job):

    """ Handler function that will be used to process jobs. """
    job_input = job['input']

    print("Downloading example.mp3")
    url = "https://github.com/deezer/spleeter/raw/master/audio_example.mp3"
    destination_path = "example.mp3"
    urllib.request.urlretrieve(url, destination_path)
    print("Downloaded example.mp3")

    print("Initializing separator")
    demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", "example.mp3"])
    print("Separation done")
    name = job_input.get('name', 'World')
    return f"You are THE BEST <3, {name}!"

if not os.environ.get("DEV", False):
    runpod.serverless.start({"handler": handler})
else:
    # serve this using fastapi
    import uvicorn
    from fastapi import FastAPI
    import json
    
    app = FastAPI()

    @app.get("/")
    def test_handler():
        # read json from file
        with open("test_job.json", "r") as f:
            job = json.load(f)
        return handler(job)
    
    # run uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=80)
