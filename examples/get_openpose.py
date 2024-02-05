import os 
import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to construct an openpose skeleton file path.
"""


if __name__ == "__main__":

    # example capture_dir and handover_idx and cam idx
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

    # construct the openpose path
    openpose_path = du.construct_openpose_path(capture_dir,handover_idx, cam_idx, G_frame_index)
    
    # load the openpose path with loader
    openpose_skeleton_file = du.loader(openpose_path)

    # select, for example, the first skeleton in the file, access and reshape the coordinate points
    skeleton = np.reshape(np.array(openpose_skeleton_file["people"][0]["pose_keypoints_2d"]), (25,3))

    # reorganize the skeleton data
    skeleton_xs, skeleton_ys, skeleton_confs = du.organize_openpose_skeleton(skeleton)
    
    print(f"the first OpenPose skeleton for frame {G_frame_index}, camera {cam_idx}:")
    print(f"x coordinates:     {skeleton_xs}")
    print(f"y coordinates:     {skeleton_ys}")
    print(f"confidence values: {skeleton_confs}")