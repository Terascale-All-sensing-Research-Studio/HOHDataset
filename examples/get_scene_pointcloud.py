import os 
import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to retrieve a full scene point cloud.
"""


if __name__ == "__main__":

    # example capture_dir and handover_idx
    capture_dir = "01638-46157-S1"
    handover_idx = "1"

    # construct metadata json file path
    this_capture_metadata_path = du.construct_capture_metadata_path(capture_dir)
   
    # load the metadata
    this_capture_metadata = du.loader(this_capture_metadata_path)
   
    # get the metadata for this particular handover
    this_handover_metadata = du.get_this_handover_metadata(this_capture_metadata, handover_idx)

    # retrieve the keyframes dict
    handover_keyframes = this_handover_metadata["keyframes"]

    # access the G frame index
    G_frame_index = handover_keyframes["g_frame_index"]
    
    # construct a scene point cloud path
    scene_ptcld_path = du.construct_scene_pointcloud_path(capture_dir, handover_idx, G_frame_index)

    # load the pointcloud
    scene_ptcld = du.loader(scene_ptcld_path)

    print(f"Scene pointcloud for frame {G_frame_index} has {len(scene_ptcld.vertices)} vertices")