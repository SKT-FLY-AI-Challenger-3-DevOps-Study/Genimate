import torch

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