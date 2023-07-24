import torch
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
from utils import *
import numpy as np
from lora_diffusion import patch_pipe, tune_lora_scale
from PIL import Image

model_id = "runwayml/stable-diffusion-v1-5"
device = device_loader()

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(
    device
)
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
torch.manual_seed(100)
patch_pipe(
    pipe,
    "AI/models/final_lora.safetensors",
    patch_text=True,
    patch_ti=True,
    patch_unet=True,
)

torch.manual_seed(10)
np.random.seed(10)

prompt = "smile sktadot boy under the sunlight."
prompt = "boy holding an umbrella, sktadot, rainy day"
tune_lora_scale(pipe.unet, 1.0)
tune_lora_scale(pipe.text_encoder, 1.0)
image = pipe(prompt, num_inference_steps=20, guidance_scale=7).images[0]
image.save("AI/outputs/adot_rain.png")