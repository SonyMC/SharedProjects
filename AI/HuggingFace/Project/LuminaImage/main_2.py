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

# Check if ROCm is available for AMD GPU
rocm_available = False
try:
    # Check if PyTorch was built with ROCm support
    if torch.version.hip is not None:
        rocm_available = torch.cuda.is_available()  # In PyTorch, ROCm uses the cuda namespace
        if rocm_available:
            torch.backends.cudnn.benchmark = True
            logging.info(f"Using AMD GPU: {torch.cuda.get_device_name(0)}")
            logging.info(f"ROCm version: {torch.version.hip}")
except (AssertionError, RuntimeError, AttributeError) as e:
    logging.warning(f"ROCm not properly supported by PyTorch: {str(e)}")
    rocm_available = False
    
if not rocm_available:
    logging.info("ROCm not available, falling back to CPU for computation")

# Set device and dtype appropriately (cuda namespace is used for ROCm in PyTorch)
device = "cuda" if rocm_available else "cpu"
# Use float32 for CPU as bfloat16 may not be supported
dtype = torch.bfloat16 if rocm_available else torch.float32

# Load the model with appropriate settings
pipe = Lumina2Pipeline.from_pretrained(
    "Alpha-VLLM/Lumina-Image-2.0", 
    torch_dtype=dtype
)

# Enable model offloading if ROCm is available, otherwise use CPU
if rocm_available:
    pipe = pipe.to("cuda")
    # Optionally enable model CPU offload to conserve VRAM if needed
    # pipe.enable_model_cpu_offload()
    logging.info("Model loaded on AMD GPU. Image generation will be accelerated.")
else:
    pipe = pipe.to("cpu")
    logging.info("Model loaded on CPU. Image generation may be slow.")

prompt = "Potray the poem Lord Ullin's daughter in a fantasy style, with a focus on the themes of love and danger. The scene should be set on a stormy night, with a dramatic sky and turbulent waters. The characters should be depicted in a romantic yet perilous situation, capturing the essence of the poem's narrative. The artwork should evoke a sense of urgency and emotion, with vivid colors and dynamic lighting to enhance the atmosphere."

# If using AMD GPU, we can use higher resolution and more steps
height = 1024 if rocm_available else 768
width = 1024 if rocm_available else 768
steps = 50 if rocm_available else 30

image = pipe(
    prompt,
    height=height,
    width=width,
    guidance_scale=4.0,
    num_inference_steps=steps,
    cfg_trunc_ratio=0.25,
    cfg_normalization=True,
    generator=torch.Generator("cpu").manual_seed(0)  # Keep seed generator on CPU
).images[0]
image.save("lumina_demo.png")

# Optional: Clean up to free memory
del pipe
gc.collect()

# Safely clear CUDA/ROCm cache if available
if rocm_available:
    try:
        torch.cuda.empty_cache()
    except:
        pass
