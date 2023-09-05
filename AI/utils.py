import torch
from PIL import Image

def device_loader():
    print(torch.cuda.is_available())
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
        
        # if torch.backends.mps.is_available():
        #     device = torch.device('mps')
        # else:
        #     device = torch.device('cpu')
            
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