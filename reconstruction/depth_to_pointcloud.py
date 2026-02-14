import numpy as np
import open3d as o3d
from PIL import Image
from pathlib import Path


class DepthToPointCloud:
    """
    Converts RGB image + depth map into a 3D point cloud
    """

    def run(
        self,
        image_path: Path,
        depth_path: Path,
        output_path: Path,
        depth_scale: float = 1000.0,
        depth_trunc: float = 5.0
    ):
        # Load RGB
        color = np.array(Image.open(image_path).convert("RGB"))

        # Load depth
        depth = np.load(depth_path).astype(np.float32)

        # Create Open3D images
        color_o3d = o3d.geometry.Image(color)
        depth_o3d = o3d.geometry.Image(depth)

        # Fake pinhole camera (OK for now)
        h, w = depth.shape
        intrinsic = o3d.camera.PinholeCameraIntrinsic(
            w, h, fx=w, fy=h, cx=w / 2, cy=h / 2
        )

        # Create RGBD image
        rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
            color_o3d,
            depth_o3d,
            depth_scale=depth_scale,
            depth_trunc=depth_trunc,
            convert_rgb_to_intensity=False
        )

        # Generate point cloud
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
            rgbd, intrinsic
        )

        # Flip for correct orientation
        pcd.transform([[1, 0, 0, 0],
                       [0, -1, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, 1]])

        output_path.parent.mkdir(parents=True, exist_ok=True)
        o3d.io.write_point_cloud(str(output_path), pcd)

        return pcd
