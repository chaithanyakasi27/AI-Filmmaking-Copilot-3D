import torch
import numpy as np
from PIL import Image
from pathlib import Path
from transformers import pipeline


class DepthAnythingRunner:
    """
    Uses Depth Anything via HuggingFace Transformers
    """

    def __init__(self, device=None):
        if device is None:
            device = 0 if torch.cuda.is_available() else -1

        self.pipe = pipeline(
            task="depth-estimation",
            model="LiheYoung/depth-anything-base-hf",
            device=device
        )

    def run(self, image_path: Path, output_path: Path):
        image = Image.open(image_path).convert("RGB")

        result = self.pipe(image)
        depth = result["depth"]

        depth_np = np.array(depth)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(output_path, depth_np)

        return depth_np
