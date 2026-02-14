from pathlib import Path
from reconstruction.depth_to_pointcloud import DepthToPointCloud

SCENE_ID = "scene_001"

converter = DepthToPointCloud()

pcd = converter.run(
    image_path=Path(f"data/scenes/{SCENE_ID}/images/front.png"),
    depth_path=Path(f"data/scenes/{SCENE_ID}/depth/front.npy"),
    output_path=Path(f"data/scenes/{SCENE_ID}/pointclouds/front.ply")
)

print("Point cloud points:", len(pcd.points))
