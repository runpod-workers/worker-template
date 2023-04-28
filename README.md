<div align="center">

<h1>Template | Worker</h1>

[![Docker Image](https://github.com/runpod-workers/worker-template/actions/workflows/CD-docker_build.yml/badge.svg)](https://github.com/runpod-workers/worker-template/actions/workflows/CD-docker_build.yml)

🚀 | A simple worker that can be used as a starting point to build your own custom RunPod Endpoint API worker.
</div>

## 📖 | Getting Started

1. Clone this repository.
2. Add your code to the `src` directory.
3. Update the `handler.py` file to load models and process requests.
4. Add any dependencies to the `requirements.txt` file.
5. Update the `Dockerfile` to include any additional dependencies.

### CI/CD

This repository is setup to automatically build and push a docker image to the GitHub Container Registry. You will need to add your DockerHub credentials `DOCKERHUB_USERNAME` & `DOCKERHUB_TOKEN` to the GitHub Secrets for this repository to enable this functionality.

## Best Practices

Models should be part of your docker image, this can be accomplished by either copying them into the image or downloading them during the build process.
