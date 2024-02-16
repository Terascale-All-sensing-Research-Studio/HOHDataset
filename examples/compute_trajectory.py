import os

import numpy as np
import trimesh

import constants
import data_utils as du


"""
This file contains an example of how to compute a target trajectory 
over the course of a full handover.
"""


if __name__ == "__main__":
    # example capture_dir, handover_idx, and target
    capture_dir = "01638-46157-S1"
    handover_idx = 0
    target = "giver" 

    # isolate keyframes, as shown in get_keyframes.py
    reference_meta_data_path = du.construct_capture_metadata_path(capture_dir)
    reference_meta_data = du.loader(reference_meta_data_path)
    handover_metadata = du.get_this_handover_metadata(reference_meta_data, handover_idx)
    handover_keyframes = handover_metadata["keyframes"]

    # iterate over all segmented point clouds, saving centroid to the trajectory
    trajectory_points = []
    for frame_idx in range(handover_keyframes["g_frame_index"], handover_keyframes["r_frame_index"]):
        # load segmented point cloud, as shown in get_segmented_pointcloud.py
        segmented_ptcld = du.loader(du.construct_segmented_pointcloud_path(capture_dir, handover_idx, frame_idx, target))
        trajectory_points.append(np.mean(segmented_ptcld.vertices, axis=0))

    print(f"found center of mass over {len(trajectory_points)} frames for target: {target} ")