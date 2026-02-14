from pathlib import Path
from reconstruction.pointcloud_fusion import PointCloudFusion

SCENE_ID = "scene_001"

fusion = PointCloudFusion()

pcd = fusion.run(
    pointcloud_paths=[
        Path(f"data/scenes/{SCENE_ID}/pointclouds/front.ply"),
        Path(f"data/scenes/{SCENE_ID}/pointclouds/left.ply"),
        Path(f"data/scenes/{SCENE_ID}/pointclouds/right.ply"),
        Path(f"data/scenes/{SCENE_ID}/pointclouds/top.ply"),
    ],
    output_path=Path(f"data/scenes/{SCENE_ID}/pointclouds/scene_fused.ply")
)

print("Fused point cloud points:", len(pcd.points))
