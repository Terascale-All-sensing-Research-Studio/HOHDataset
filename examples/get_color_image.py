import os 
import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to construct an color image path.
"""



if __name__ == "__main__":

    # example capture_dir and handover_idx, camera idx
    capture_dir = "01638-46157-S1"
    handover_idx = "1"
    cam_idx = 1

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
    
    # construct color image path
    color_image_path = du.construct_color_image_path(capture_dir, handover_idx, cam_idx, G_frame_index)
    
    # load the color image
    color_image = du.loader(color_image_path)
    
    print("Shape of the color image: \n", color_image.shape)