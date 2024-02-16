import os

import constants
import data_utils as du



"""
This file contains examples of how to:
    - load any Kinect color images, from the RAW data
    - load mask files for any frame, from the RAW data
    - construct paths to full point clouds for any frame, from the RAW data
"""


if __name__ == "__main__":

    # ----------load any Kinect color images-------------------
    # example capture_dir, frame_idx, and cam_idx
    capture_dir = "01638-46157-S1"
    frame_idx = 488
    cam_idx = 0

    # set up synchronized block of image paths
    # returns numpy array of shape: (num_frames, 4) (for 4 cameras)
    # this also works for depth image if modality=="depth"
    all_kcolor_image_paths = du.get_image_paths(capture_dir, modality="kcolor")

    # to get image 488 from Kinect color camera 0
    this_image_path = all_kcolor_image_paths[frame_idx, cam_idx]

    # load the image
    this_image = du.loader(this_image_path)



    # ----------load mask files for any frame------------------
    # example capture_dir, handover_idx, frame_idx, cam_idx, and target
    capture_dir = "01638-46157-S1"
    handover_idx = 0
    frame_idx = 488
    cam_idx = 0
    target = "object" 

    # get the keyframe metadata to know how many masks are in the file
    # this is like in get_keyframes.py
    reference_meta_data_path = du.construct_capture_metadata_path(capture_dir)
    reference_meta_data = du.loader(reference_meta_data_path)
    handover_metadata = du.get_this_handover_metadata(reference_meta_data, handover_idx)
    handover_keyframes = handover_metadata["keyframes"]

    # build the path to the object mask file
    mask_file_path = du.construct_raw_data_masks_path(capture_dir, cam_idx, handover_idx, target)

    # load the masks
    # this returns a (1080, 1920, num_frames) array of masks
    num_frames = handover_keyframes["r_frame_idx"] - handover_keyframes["g_frame_idx"] + 1
    masks = du.load_masks(
        path=mask_file_path,
        num_frames=num_frames
    )

    # get the relative index for this mask
    mask_idx = frame_idx - handover_keyframes["g_frame_idx"]

    # isolate this one mask
    this_mask = masks[:,:,mask_idx]



    # ----------construct paths to full point clouds for any frame------------------
    # example capture_dir, handover_idx, and frame_idx
    capture_dir = "01638-46157-S1"
    handover_idx = 0
    frame_idx = 488

    pointcloud_path = du.construct_raw_data_scene_pointcloud_path(capture_dir, handover_idx, frame_idx)

    pointcloud = du.loader(pointcloud_path)
