from pathlib import Path
from depth.depth_anything_runner import DepthAnythingRunner
from reconstruction.depth_to_pointcloud import DepthToPointCloud

SCENE_ID = "scene_001"

depth_runner = DepthAnythingRunner()
pcd_runner = DepthToPointCloud()

views = ["front", "left", "right", "top"]

for view in views:
    print(f"Processing view: {view}")

    image_path = Path(f"data/scenes/{SCENE_ID}/images/{view}.png")
    depth_path = Path(f"data/scenes/{SCENE_ID}/depth/{view}.npy")
    pcd_path = Path(f"data/scenes/{SCENE_ID}/pointclouds/{view}.ply")

    # Depth
    depth_runner.run(
        image_path=image_path,
        output_path=depth_path
    )

    # Point cloud
    pcd = pcd_runner.run(
        image_path=image_path,
        depth_path=depth_path,
        output_path=pcd_path
    )

    print(f"  → Points: {len(pcd.points)}")

print("All views processed")
