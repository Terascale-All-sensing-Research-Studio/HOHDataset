import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to retrieve the keyframe indices for a
particular handover using the metadata.
"""

if __name__ == "__main__":
    # example capture_dir and handover_idx 
    capture_dir = "01638-46157-S1"
    handover_idx = "1"

    # construct metadata json file path
    reference_meta_data_path = du.construct_capture_metadata_path(capture_dir)
   
    # load the metadata
    reference_meta_data = du.loader(reference_meta_data_path)
   
    # get the metadata for this particular handover
    handover_metadata = du.get_this_handover_metadata(reference_meta_data, handover_idx)
    
    # retrieve the keyframes dict
    handover_keyframes = handover_metadata["keyframes"]
   
    # access as follows:
    print(f" Interaction {capture_dir}_{handover_idx} has keyframes: ")
    print(f'   O frame index: {handover_keyframes["o_frame_index"]} ')
    print(f'   G frame index: {handover_keyframes["g_frame_index"]} ')
    print(f'   T frame index: {handover_keyframes["t_frame_index"]} ')
    print(f'   R frame index: {handover_keyframes["r_frame_index"]} ')
