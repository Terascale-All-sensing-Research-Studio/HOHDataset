import os 
import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to get masks for 
a particular frame and camera for a particular handover.
"""

if __name__ == "__main__":
    # An example capture_dir and handover_idx
    # will retrieve the G frame object mask from camera 0 
    capture_dir = "01638-46157-S1"
    handover_idx = "1"
    cam_idx = 0
    target = "object"
    
    # construct metadata json file path
    this_capture_metadata_path = du.construct_capture_metadata_path(capture_dir)
   
    # load the metadata
    this_capture_metadata = du.loader(this_capture_metadata_path)
   
    # get the metadata for this particular handover
    this_handover_metadata = du.get_this_handover_metadata(this_capture_metadata, handover_idx)
    
    # retrieve the keyframes dict
    handover_keyframes = this_handover_metadata["keyframes"]

    # retrieve the G frame index
    G_frame_index = handover_keyframes["g_frame_index"]
    
    # construct the mask path for the G frame
    mask_path = du.construct_mask_path(capture_dir, handover_idx, cam_idx, target, G_frame_index)
    
    # use load masks to load the masks from the mask path
    # NOTE: when loading a file containing multiple masks,
    #       set num_frames = range_end - range_start + 1
    obj_mask = du.load_masks(mask_path, num_frames=1)
    