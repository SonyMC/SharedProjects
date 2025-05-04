import torch
from diffusers import Lumina2Pipeline
import os
from PIL import Image
import gc
import logging
from dotenv import load_dotenv

# Optional: Load environment variables
load_dotenv()

# Optional: Setup logging
logging.basicConfig(level=logging.INFO)

# Check if CUDA is available and properly supported by the PyTorch installation
cuda_available = False
try:
    cuda_available = torch.cuda.is_available()
    if cuda_available:
        torch.backends.cudnn.benchmark = True
        logging.info(f"Using GPU: {torch.cuda.get_device_name(0)}")
except (AssertionError, RuntimeError) as e:
    logging.warning(f"CUDA not properly supported by PyTorch: {str(e)}")
    cuda_available = False
    
if not cuda_available:
    logging.info("Using CPU for computation")

# Set device and dtype appropriately
device = "cuda" if cuda_available else "cpu"
# Use float32 for CPU as bfloat16 may not be supported on CPU
dtype = torch.bfloat16 if cuda_available else torch.float32

# Load the model with appropriate settings
pipe = Lumina2Pipeline.from_pretrained(
    "Alpha-VLLM/Lumina-Image-2.0", 
    torch_dtype=dtype
)

# Enable model CPU offload if CUDA is available, otherwise use CPU
if cuda_available:
    pipe.enable_model_cpu_offload()
else:
    pipe = pipe.to("cpu")
    logging.info("Model loaded on CPU. Image generation may be slow.")

#prompt = "A serene photograph capturing the golden reflection of the sun on a vast expanse of water. The sun is positioned at the top center, casting a brilliant, shimmering trail of light across the rippling surface. The water is textured with gentle waves, creating a rhythmic pattern that leads the eye towards the horizon. The entire scene is bathed in warm, golden hues, enhancing the tranquil and meditative atmosphere. High contrast, natural lighting, golden hour, photorealistic, expansive composition, reflective surface, peaceful, visually harmonious."
prompt = "A highwayman riding on a horse into the night. The horse is galloping, and the rider is wearing a dark cloak. The moonlight casts a silver glow on the scene, illuminating the rider's face, which is partially obscured by a wide-brimmed hat. The background features a dense forest, with shadows dancing among the trees. The atmosphere is tense and mysterious, evoking a sense of adventure and danger. The image captures the essence of a classic tale of intrigue and heroism, with a focus on the dynamic movement of the horse and rider."
image = pipe(
    prompt,
    height=768,  # Reduced resolution for CPU usage
    width=768,   # Reduced resolution for CPU usage
    guidance_scale=4.0,
    num_inference_steps=30,  # Reduced steps for CPU usage
    cfg_trunc_ratio=0.25,
    cfg_normalization=True,
    generator=torch.Generator("cpu").manual_seed(0)
).images[0]
image.save("lumina_demo.png")

# Optional: Clean up to free memory
del pipe
gc.collect()

# Safely clear CUDA cache if available
if cuda_available:
    try:
        torch.cuda.empty_cache()
    except:
        pass
