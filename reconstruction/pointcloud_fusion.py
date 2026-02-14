import open3d as o3d
from pathlib import Path
from typing import List


class PointCloudFusion:
    """
    Merges multiple point clouds into a single scene-level cloud
    """

    def run(
        self,
        pointcloud_paths: List[Path],
        output_path: Path,
        voxel_size: float = 0.02
    ):
        pcds = []

        for path in pointcloud_paths:
            pcd = o3d.io.read_point_cloud(str(path))
            pcds.append(pcd)

        # Merge
        fused = o3d.geometry.PointCloud()
        for pcd in pcds:
            fused += pcd

        # Downsample (important for stability)
        fused = fused.voxel_down_sample(voxel_size=voxel_size)

        # Estimate normals (needed for meshing)
        fused.estimate_normals(
            search_param=o3d.geometry.KDTreeSearchParamHybrid(
                radius=0.1, max_nn=30
            )
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        o3d.io.write_point_cloud(str(output_path), fused)

        return fused
