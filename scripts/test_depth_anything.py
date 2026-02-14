from pathlib import Path
from depth.depth_anything_runner import DepthAnythingRunner

# 🔹 Use an existing scene folder
SCENE_ID = "scene_001"   # change if needed

runner = DepthAnythingRunner()

depth = runner.run(
    image_path=Path(f"data/scenes/{SCENE_ID}/images/front.png"),
    output_path=Path(f"data/scenes/{SCENE_ID}/depth/front.npy")
)

print("Depth map shape:", depth.shape)
