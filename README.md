![RunPod Worker Template](https://5ccaof7hvfzuzf4p.public.blob.vercel-storage.com/6alBFvrkrTGIkdpWJeawe_image-tXkyfhuu51FV41RaT5CsBS0xOZqlHO.jpeg)

This repository serves as a starting point for creating your own custom RunPod Serverless worker. It provides a basic structure and configuration that you can build upon.

## Getting Started

1.  **Use this template:** Create a new repository based on this template or clone it directly.
2.  **Customize:** Modify the code and configuration files to implement your specific task.
3.  **Test:** Run your worker locally to ensure it functions correctly.
4.  **Deploy:** Connect your repository to RunPod or build and push the Docker image manually.

## Customizing Your Worker

- **`src/handler.py`:** This is the core of your worker.
  - The `handler(event)` function is the entry point executed for each job.
  - The `event` dictionary contains the job input under the `"input"` key.
  - Modify this function to load your models, process the input, and return the desired output.
  - Consider implementing model loading outside the handler (e.g., globally or in an initialization function) if models are large and reused across jobs.
- **`requirements.txt`:** Add any Python libraries your worker needs to this file. These will be installed via `uv` when the Docker image is built.
- **`Dockerfile`:**
  - This file defines the Docker image for your worker.
  - It starts from a RunPod base image (`runpod/base`) which includes CUDA and common dependencies.
  - It installs dependencies from `requirements.txt` using `uv`.
  - It copies your `src` directory into the image.
  - You might need to add system dependencies (`apt-get install ...`), environment variables (`ENV`), or other setup steps here if required by your specific application.
- **`test_input.json`:** Modify this file to provide relevant sample input for local testing.

## Testing Locally

You can test your handler logic locally using the RunPod Python SDK.

1.  **Create & Activate Virtual Environment:**

    ```bash
    # Create venv (replace 'python3' if needed)
    python3 -m venv venv

    # Activate venv
    # macOS/Linux:
    source venv/bin/activate
    # Windows:
    .\venv\Scripts\activate
    ```

2.  **Install Dependencies:**

    ```bash
    # Install requirements for local testing (includes runpod SDK)
    # Ensure you have uv installed or use pip: pip install -r requirements.txt
    uv pip install -r requirements.txt
    ```

3.  **Run the Handler:**
    ```bash
    # The script automatically uses test_input.json
    python src/handler.py
    ```
    This will execute your `handler` function with the contents of [`test_input.json`](/test_input.json) as input.

## Deploying to RunPod

There are two main ways to deploy your worker:

1.  **GitHub Integration (Recommended):**

    - Push your customized code to a GitHub repository.
    - In the RunPod Serverless UI, create a new Template or Endpoint and connect it to your GitHub repository.
    - RunPod will automatically build the Docker image using the `Dockerfile` in your repository whenever you push changes (if auto-deploy is enabled).

2.  **Manual Docker Build & Push:**
    - Build the Docker image:
      ```bash
      # Replace with your registry username and image name/tag
      docker build -t your-dockerhub-username/your-image-name:latest --platform linux/amd64 .
      ```
    - Push the image to a container registry (like Docker Hub, GHCR, etc.):
      ```bash
      # Log in to your registry if needed (e.g., docker login)
      docker push your-dockerhub-username/your-image-name:latest
      ```
    - In the RunPod Serverless UI, create a new Template or Endpoint and point it to the image you pushed in your container registry.

## Further Information

- **RunPod Serverless Documentation:** [https://docs.runpod.io/serverless/overview](https://docs.runpod.io/serverless/overview)
- **Python SDK:** [https://github.com/runpod/runpod-python](https://github.com/runpod/runpod-python)
- **Base Docker Images:** [https://github.com/runpod/containers/tree/main/official-templates/base](https://github.com/runpod/containers/tree/main/official-templates/base)
- **Community Discord:** [https://runpod.io/discord](https://runpod.io/discord)
