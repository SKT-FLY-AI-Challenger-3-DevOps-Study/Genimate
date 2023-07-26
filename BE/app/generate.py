import torch
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
import numpy as np
from lora_diffusion import patch_pipe, tune_lora_scale
from PIL import Image
from random import uniform
from datetime import datetime
from fastapi import APIRouter
from apscheduler.schedulers.background import BackgroundScheduler
import os

from app import get_weather

generate_router = APIRouter()
scheduler = BackgroundScheduler()

def device_loader():
    print(torch.cuda.is_available())
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
        
    return device

def is_black_image(img):
    try:
        img_data = img.getdata()
        for pixel in img_data:
            if pixel != (0, 0, 0):  # Check for non-black pixels (considering RGBA)
                return False
        return True
    except Exception as e:
        print("Error:", e)
        return False

# cpu버전에선 torch_dtype=torch.float16 삭제해야함 
# pip install diffusers==0.14.0
def generate_adot(prompt:str, seed:int):
    model_id = "runwayml/stable-diffusion-v1-5"
    device = device_loader()

    # pip install diffusers==0.14.0
    pipe = StableDiffusionPipeline.from_pretrained(model_id).to(
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

def run():
    prompt = get_weather.forecast()
    seed = int(uniform(0,100))
    result = generate_adot(prompt, seed)

    while(is_black_image(result)):
        result = generate_adot(prompt, seed)

    result.save(os.path.join('images', datetime.now().strftime("%Y%m%d%H%M%S") + '.png'))

@generate_router.on_event("startup")
async def generate_scheduler():
    scheduler.add_job(run, 'cron', hour=15, minute=15, timezone="Asia/Seoul")
    scheduler.start()
    
@generate_router.on_event("shutdown")
async def shutdown_scheduler():
    scheduler.shutdown()