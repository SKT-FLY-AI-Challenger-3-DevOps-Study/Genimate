import torch
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
from utils import *
import numpy as np
from lora_diffusion import patch_pipe, tune_lora_scale
from PIL import Image
from random import uniform
import time

def generate_adot(prompt:str, seed:int):
    model_id = "runwayml/stable-diffusion-v1-5"
    device = device_loader()

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(
        device
    )
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    patch_pipe(
        pipe,
        "AI/models/final_lora.safetensors",
        patch_text=True,
        patch_ti=True,
        patch_unet=True,
    )

    torch.manual_seed(seed)
    np.random.seed(seed)

    tune_lora_scale(pipe.unet, 1.0)
    tune_lora_scale(pipe.text_encoder, 1.0)

    image = pipe(prompt, num_inference_steps=20, guidance_scale=6.5).images[0]

    return image

if __name__ == "__main__":
    # test용 prompt
    # prompt = "smile sktadot boy under the sunlight."
    prompt = "A sktadot enjoying a picnic under a clear blue sky, perfect face"
    prompt = "A sktadot smiling under a clear blue sky, perfect face"
    
    # prompt = "A sktadot building a snowman on a snowy day, perfect face"
    # prompt = "A smile sktadot ice skating on a frozen lake on a snowy day, perfect face"
    # prompt = "A sktadot, perfect face, cute face"
    # prompt = "A sktadot exploring the mountains under a clear sky, perfect face"
    # prompt = "photo of sktadot, sharp, hyper realistic, perfect face, rainy day" 
    # prompt = "rainy day, sktadot boy, cute, rain, water, artstation, 8k --ar 2:3 --uplight" # 비오는날
    # prompt = "A sktadot walking under the many of clouds, cloudy day, blue sky, perfect face" # 흐린 날
    
    seed  = int(uniform(0,100))

    result = generate_adot(prompt, seed)

    while(is_black_image(result)):
        result = generate_adot(prompt, seed)

    timestr = time.strftime("%Y%m%d-%H%M%S")    
    result.save("AI/outputs/adot_"+timestr+"_"+str(seed)+".png")
