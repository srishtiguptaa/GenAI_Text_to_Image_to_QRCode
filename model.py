from platform import python_version
print(python_version())
pip install torch==2.3.1 torchvision==0.18.1+cu121 torchaudio==2.3.1+cu121 fastai==2.7.15
pip install diffusers
import torch
from PIL import Image
from diffusers import StableDiffusionControlNetImg2ImgPipeline, ControlNetModel, DDIMScheduler, StableDiffusionPipeline
from diffusers.utils import load_image
import base64
from io import BytesIO

# Initialize the Stable Diffusion text-to-image pipeline
text2img_pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16
)


# text2img_pipe.enable_xformers_memory_efficient_attention()
text2img_pipe.enable_model_cpu_offload()
# prompt=input()
prompt = "a place in paris with full eiffel tower, realistic, 8K, fantasy".

#### Example of additional information you want to enter 
url = "https://www.samsung.com/in/"
pip install qrcode[pil]
import qrcode
from PIL import Image
from IPython.display import display

# Define the URL to be encoded in the QR code

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white').convert('RGB')

# Resize the image to the desired resolution
img = img.resize((1720, 1720), Image.ANTIALIAS)

# Save the image to a file
img.save("qr_code_1720x1720.png")

# Display the image in the notebook
display(img)

# Set a manual seed for reproducibility
generator = torch.manual_seed(123121231)

# Generate the initial image from the prompt
text2img_image = text2img_pipe(
    prompt=prompt,
    guidance_scale=7.5,
    generator=generator,
    num_inference_steps=50,
    height=768,
    width=768
)

# Display the generated image
text2img_image.images[0]

controlnet = ControlNetModel.from_pretrained(
    "DionTimmer/controlnet_qrcode-control_v11p_sd21",
    torch_dtype=torch.float16
)

pipe = StableDiffusionControlNetImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    controlnet=controlnet,
    safety_checker=None,
    torch_dtype=torch.float16
)

# pipe.enable_xformers_memory_efficient_attention()
# pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

def resize_for_condition_image(input_image: Image, resolution: int):
    input_image = input_image.convert("RGB")
    W, H = input_image.size
    k = float(resolution) / min(H, W)
    H *= k
    W *= k
    H = int(round(H / 64.0)) * 64
    W = int(round(W / 64.0)) * 64
    img = input_image.resize((W, H), resample=Image.LANCZOS)
    return img

# qr code image
# qr_code_image = load_image("/kaggle/input/my-qrcode/qr.png")
qr_code_image = img
qr_code_image = resize_for_condition_image(qr_code_image, 768)

# base image
base_image = text2img_image.images[0]
base_image = resize_for_condition_image(base_image, 768)


# play with guidance_scale, controlnet_conditioning_scale and strength to vary
# the dominance of the QR Code vs the base image and prompt

# Approximate optimal default value
#   guidance_scale = 20,
#   controlnet_conditioning_scale = 2.0,
#   strength = 0.9

generator = torch.manual_seed(123121231)
image = pipe(
#     prompt="black and white tajmahal,  realistic, 8K, fantasy",
    prompt=prompt,
    negative_prompt="ugly, disfigured, low quality, blurry, nsfw",
    image=base_image,
    control_image=qr_code_image,
    width=768,
    height=768,
    guidance_scale=50,
    controlnet_conditioning_scale=3.0,
    generator=generator,
    strength=0.9,
    num_inference_steps=150
)

image.images[0]


