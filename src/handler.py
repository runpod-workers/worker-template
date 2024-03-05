""" Example handler file. """

import os
import runpod
import dotenv
import urllib.request
import demucs.separate
import boto3

dotenv.load_dotenv()
s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_S3_ACCESS_ID'), aws_secret_access_key=os.environ.get('AWS_S3_ACCESS_KEY'))

def handler(job):

    """ Handler function that will be used to process jobs. """
    job_input = job['input']
    song_name = job_input.get('song_name')
    url = job_input.get('url')

    print(f"Downloading {song_name}")
    destination_path = f"{song_name}.mp3"
    urllib.request.urlretrieve(url, destination_path)
    print(f"Downloaded {song_name}")

    print("Downloaded file path: ", destination_path)
    print("Current working directory: ", os.getcwd())

    print("Initializing separator")
    demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", f"{song_name}.mp3"])
    print("Separation done")
    
    s3.upload_file(f"separated/mdx_extra/{song_name}/vocals.mp3", 'auto-karaoke', f'{song_name}/vocals.mp3')
    s3.upload_file(f"separated/mdx_extra/{song_name}/no_vocals.mp3", 'auto-karaoke', f'{song_name}/no_vocals.mp3')

    return f"Uploaded spleeeted!"

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
