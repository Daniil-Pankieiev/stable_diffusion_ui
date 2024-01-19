# Stable Diffusion UI

This is a simple web interface for generating images using the Stable Diffusion model. It allows users to select a model, input a prompt, and specify the dimensions of the generated image.

## Prerequisites

- Docker
- NVIDIA Docker (if you're using NVIDIA GPUs)

## Building the Docker Image

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the directory containing the Dockerfile.

3. Run the following command to build the Docker image:

    ```bash
    docker build -t stable_diffusion_ui .
    ```

## Running the Docker Container

After the image is built, you can run the container with the following command:

```bash
docker run --gpus all -p 5000:5000 stable_diffusion_ui
```
The --gpus all flag is used to make the GPU available to the container. If you're not using a GPU, you can omit this flag.

## Another way to run
Alternative command (`python3 -m flask run`) if they encounter any issues with the Docker container.


## Using the Web Interface
1. Select a model from the dropdown menu.
2. Enter a prompt in the "Prompt" field.
3. Optionally, enter a negative prompt in the "Negative Prompt" field.
4. Specify the width and height of the generated image.
5. Click the "Generate" button to generate the image.

## Models
### The following models are currently available:
- StableDiffusion 1.5
