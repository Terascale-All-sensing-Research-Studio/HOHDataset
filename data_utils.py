""" 
This file contains functions that load each type of data in the
HOH Minimum Dataset and HOH Keyframes Dataset
"""

import os
import json

import numpy as np
import trimesh
from PIL import Image


import constants


def loader(path):
    extension = path.split(".")[-1]
    if extension in ["jpg", "png"]:
        return np.array(Image.open(path))
    elif extension in ["ply", "obj", "stl"]:
        return trimesh.load(path)
    elif extension in ["npy", "npz"]:
        return np.load(path)
    elif extension == "json":
        return json.load(open(path, "r"))
    elif extension == "json":
        return json.load(open(path, "r"))
    else:
        print(f"unrecognized file extension: {extension}")

def construct_segmented_pointcloud_path(capture_dir, handover_idx, frame_idx, target):
    """ 
    constructs path to a segmented point cloud.
    simply use loader() to load this file path.
    """
    assert target in ["giver", "receiver", "object"], "please pass valid path: [giver, receiver, object]"
    return constants.SEGMENTED_POINTCLOUD_PATH.format(capture_dir, handover_idx, target, frame_idx)

def construct_scene_pointcloud_path(capture_dir, handover_idx, frame_idx):
    """ 
    constructs path to a full scene point cloud.
    simply use loader() to load this file path.
    """
    return constants.SCENE_POINTCLOUD_PATH.format(capture_dir, handover_idx, frame_idx)

def construct_3dm_align_path(capture_dir, handover_idx):
    """
    constructs path to the 3d model alignments file.
    simply use loader() to load this file path.
    """
    return constants.THREEDM_ALIGNMENTS_PATH.format(capture_dir, capture_dir, handover_idx)

def get_3dm_alignment_to_frame(alignments_dict, keyframes_dict, frame_idx):
    """
    returns a 4x4 transformation matrix that will align the object 3D model
    to the scene at frame frame_idx using trimesh.TriMesh.apply_transform().
    - alignments_dict is from loader(construct_3dm_align_path()).
    - keyframes_dict is a dict containing keys <O_frame_index>, <G_frame_index>, 
      <T_frame_index>, <R_frame_index> (from get_this_handover_metadata()).
    - frame_idx is the frame index that you wish to align to.
    """
    transform = np.array(alignments_dict["3dm_to_O"])
    if frame_idx == keyframes_dict["o_frame_index"]:
        return transform
       
    transform = np.array(alignments_dict["{}_{}".format(keyframes_dict["o_frame_index"], keyframes_dict["g_frame_index"])]) @ transform
    if frame_idx == keyframes_dict["g_frame_index"]:
        return transform
    
    for i in range(keyframes_dict["g_frame_index"]+1, frame_idx+1):
        transform = np.array(alignments_dict[f"{i-1}_{i}"]) @ transform
    return transform

def construct_capture_metadata_path(capture_dir):
    """
    constructs path to the capture reference metadata file. 
    simply use loader() to load this file path.
    """
    return constants.METADATA_PATH.format(capture_dir, capture_dir)

def get_this_handover_metadata(reference_metadata, handover_idx):
    """
    takes reference_metadata from file loaded from construct_capture_metadata_path(),
    returns dict containing all metadata associated with a particular interaction index
    """
    return {
        "left_seated_giver" : reference_metadata["left_seated_giver"],
        "object_used" : reference_metadata["objects_used"][int(handover_idx)],
        "keyframes" : reference_metadata["keyframes"][int(handover_idx)],
        "giver_receiver_comfort_ratings" : reference_metadata["giver_receiver_comfort_ratings"][int(handover_idx)],
        "giver_receiver_handedness" : reference_metadata["giver_receiver_handedness"][int(handover_idx)],
        "giver_receiver_grasp_taxonomy" : reference_metadata["giver_receiver_grasp_taxonomy"][int(handover_idx)],
        "capture_set" : reference_metadata["capture_set"]
    }

def construct_color_image_path(capture_dir, handover_idx, cam_idx, frame_idx):
    """
    constructs path to a Kinect color image.
    simply use loader() to load this file path.
    """
    return constants.KCOLOR_IMAGE_PATH.format(capture_dir, handover_idx, cam_idx, cam_idx, frame_idx)

def construct_mask_path(capture_dir, handover_idx, cam_idx, target, frame_idx):
    """
    constructs path to a segmentation mask file.
    use load_masks() to load this file path.
    """
    return constants.KCOLOR_MASK_PATH.format(capture_dir, handover_idx, cam_idx, target, frame_idx, cam_idx)

def load_masks(path, num_frames=1, mask_height=1080, mask_width=1920):
    """
    loads and unpacks mask files. 
    returns (1080, 1920, num_frames) array of binary masks.
    for full capture: num_frames = R_frame_index - G_frame_index + 1
    otherwise:        num_frames = 1
    """
    masks = np.unpackbits(loader(path)["masks"])
    masks = np.reshape(masks,(mask_height, mask_width, num_frames))
    return masks

def construct_openpose_path(capture_dir, handover_idx, cam_idx, frame_idx):
    """
    constructs path to an openpose skeleton file.
    simply use loader() to load this file path.
    """
    return constants.OPENPOSE_SKELETON_PATH.format(capture_dir, handover_idx, cam_idx, frame_idx, cam_idx)

def organize_openpose_skeleton(person_keypoints: np.ndarray):
    """
    person_keypoints should be ndarray shaped like (25, 3), representing a single skeleton.
    The cam index is the joint number per the BODY_25 OpenPose format.
    The first and second column indices are the (x, y) coordinates of the joint, respectively
    The third column is the detection confidence for that joint.
    
    returns: x points, y points, confidences
    """
    return person_keypoints[:, 0], person_keypoints[:, 1], person_keypoints[:, 2]

def construct_object_model_path(object_id, model_type="simplified"):
    """
    constructs path to an object model.
    model_type options: full, watertight, simplified, simplified_2000
    simply use loader() to load this file path.
    """
    if f"{object_id}" == "116":
        return constants.OBJECT_116_PATH
    elif f"{object_id}" == "120":
        return constants.OBJECT_120_PATH
        
    assert model_type in ["full", "watertight", "simplified", "simplified_2000"], "please pass valid model type: full, watertight, simplified, simplified_2000"
    if model_type == "full":
        return constants.OBJECT_MODEL_PATH.format("full", object_id, "cleaned")
    return constants.OBJECT_MODEL_PATH.format(model_type, object_id, model_type)
    
def construct_lookuptable_path(capture_dir):
    """
    constructs path to a lightsync lookup table, used for pulling synchronized raw Kinect image data.
    use load_lut() to load the data at this file path.
    """
    return constants.SYNC_LUT_PATH.format(capture_dir)

def load_lut(path):
    """
    loads and formats a lightsync lookup table for raw Kinect image data. 
    returns lookup table in format (num_frames, 4), where 4 is the number of cameras.
    each element is the epoch timestamp of a Kinect image.
    """
    return np.loadtxt(path, delimiter=',')

def get_image_paths(capture_dir, modality="color"):
    """
    this function should be used with RAW HOH DATA
    loads synchronization data and returns a (num_frames, 4) numpy array of paths to images.
    this array can be accessed by arr[frame_idx, cam_idx].
    simply use loader() to load individual image file paths.
    """
    assert modality in ["kcolor", "color", "depth"], "please pass valid modality in [kcolor, color, depth]"
    if modality in ["kcolor", "color"]:
        image_name_template = constants.COLOR_IMAGE_NAME
    else:
        image_name_template = constants.DEPTH_IMAGE_NAME

    # load lookup table data
    lut = load_lut(construct_lookuptable_path(capture_dir))

    # construct paths
    for timestep in range(lut.shape[0]): # for each timestep
        for cam in range(lut.shape[1]): # for each column/camera
            this_image_name = image_name_template.format(lut[timestep, cam])
            this_cam = constants.CAM_NAMES[cam]
            lut[timestep, cam] = constants.RAW_IMAGES_PATH.format(capture_dir, this_cam, this_image_name)

    return lut

def construct_raw_data_masks_path(capture_dir, cam_idx, handover_idx, target):
    """
    this function should be used with RAW HOH DATA
    constructs path to bulk mask file.
    valid targets: [giver, receiver, object]
    use load_masks() to load data at this path.
    """
    assert target in ["giver", "receiver", "object"], "please pass valid target in: [giver, receiver, object]"
    return constants.RAW_KCOLOR_MASK_PATH.format(capture_dir, cam_idx, target, handover_idx)

def construct_raw_data_object_only_masks_path(capture_dir, cam_idx, handover_idx):
    """
    this function should be used with RAW HOH DATA
    constructs path to Gpre frame object-only mask file.
    valid targets: [giver, receiver, object]
    use load_masks() to load data at this path, with num_frames=1.
    """
    return constants.RAW_KCOLOR_OBJECT_ONLY_MASK_PATH.format(capture_dir, cam_idx, handover_idx)

def construct_raw_data_openpose_path(capture_dir, handover_idx, frame_idx, cam_idx):
    """
    this function should be used with RAW HOH DATA
    constructs path to an openpose skeleton file.
    simply use loader() to load this file path.
    """
    return constants.RAW_OPENPOSE_SKELETON_PATH.format(capture_dir, handover_idx, frame_idx, cam_idx)

def construct_raw_data_scene_pointcloud_path(capture_dir, handover_idx, frame_idx):
    """
    this function should be used with RAW HOH DATA
    constructs path to a full scene point cloud file.
    simply use loader() to load this file path.
    """
    return constants.RAW_SCENE_POINTCLOUD_PATH.format(capture_dir, handover_idx, frame_idx)

def all_samples():
    """
    this function loads a list of all handover names
    according to the following scheme:
    '{}_{}'.format(capture_directory, handover_index)
    """
    return loader(constants.SAMPLES_LIST_PATH)["samples"]