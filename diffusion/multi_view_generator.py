# diffusion/multi_view_generator.py

from pathlib import Path
from typing import Dict
import torch
from diffusers import StableDiffusionPipeline
import random


class MultiViewDiffusionGenerator:
    """
    Generates multi-view diffusion images from a single cinematic prompt.
    """

    def __init__(
        self,
        model_id: str = "runwayml/stable-diffusion-v1-5",
        device: str = "cuda" if torch.cuda.is_available() else "cpu"
    ):
        self.device = device
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        self.pipe.to(self.device)

    def generate(
        self,
        visual_prompt: str,
        scene_dir: Path,
        seed: int = None
    ) -> Dict[str, Path]:
        """
        Generates front, left, right, and top views and saves them to disk.
        """
        images_dir = scene_dir / "images"
        images_dir.mkdir(parents=True, exist_ok=True)

        if seed is None:
            seed = random.randint(0, 999999)

        # Generator must match device
        if self.device == "cuda":
            generator = torch.Generator(device="cuda").manual_seed(seed)
        else:
            generator = torch.Generator().manual_seed(seed)

        views = {
            "front": "front view, centered composition",
            "left": "left side view, slight angle",
            "right": "right side view, slight angle",
            "top": "slight top-down view"
        }

        output_paths: Dict[str, Path] = {}

        for view_name, view_hint in views.items():
            prompt = f"{visual_prompt}, {view_hint}"

            image = self.pipe(
                prompt=prompt,
                num_inference_steps=30,
                guidance_scale=7.5,
                generator=generator
            ).images[0]

            output_path = images_dir / f"{view_name}.png"
            image.save(output_path)

            output_paths[view_name] = output_path

        return output_paths


# -----------------------
# Quick manual test
# -----------------------
if __name__ == "__main__":
    from agents.story_agent import StoryAgent
    from agents.visual_prompt_agent import VisualPromptAgent

    scene_dir = Path("data/scenes/scene_001")
    scene_dir.mkdir(parents=True, exist_ok=True)

    story_agent = StoryAgent()
    visual_agent = VisualPromptAgent()

    story_data = story_agent.run(
        "A dark cyberpunk alley at night with neon lights and rain"
    )
    visual_prompt = visual_agent.run(story_data)

    generator = MultiViewDiffusionGenerator()
    outputs = generator.generate(visual_prompt, scene_dir)

    print("Generated views:")
    for k, v in outputs.items():
        print(f"{k}: {v}")

    print("Done.")