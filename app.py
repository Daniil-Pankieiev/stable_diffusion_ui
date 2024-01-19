from flask import Flask, render_template, request, send_file
from diffusers import StableDiffusionPipeline
import torch

app = Flask(__name__)

# Define a dictionary to map model names to their IDs
models = {
    "StableDiffusion 1.5": "runwayml/stable-diffusion-v1-5",
    # Add more models as needed
}

# Load the models into memory
loaded_models = {name: StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda") for name, model_id in models.items()}

@app.route('/')
def home():
    return render_template('index.html', models=models.keys())

@app.route('/generate', methods=['POST'])
def generate():
    model_name = request.form['model']
    prompt = request.form['prompt']
    negative_prompt = request.form['negative_prompt']
    width = int(request.form['width'])
    height = int(request.form['height'])

    # Get the selected model
    model = loaded_models[model_name]

    image = model(prompt, negative_prompt=negative_prompt, width=width, height=height).images[0]
    image.save('output.png')

    return send_file('output.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)