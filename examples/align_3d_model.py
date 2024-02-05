import os 
import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to align an objects 3dm to 
a particular frame in a particular handover.
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
    
    # retrieve the object ID that was used
    object_used = this_handover_metadata["object_used"]
    print(f" Interaction {capture_dir}_{handover_idx} used object: {object_used}. ")

    # construct the path to the 3D model of the object
    # object ID can be ["full", "watertight", "simplified", "simplified_2000"]
    object_3dm_path = du.construct_object_model_path(object_id, model_type="simplified")
    
    # load the 3D model as a trimesh.TriMesh() object
    object_3dm = du.loader(object_3dm_path)
    print(f" object mesh {object_id} has {len(object_3dm.vertices)} vertices. ")
    
    # retrieve the keyframes dict
    handover_keyframes = this_handover_metadata["keyframes"]

    # access the G frame index
    G_frame_index = handover_keyframes["g_frame_index"]
    
    # construct 3D model alignment transforms path
    threedm_align_path = du.construct_3dm_align_path(capture_dir, handover_idx)

    # load the alignment transforms file
    transformation_json = du.loader(threedm_align_path)
    
    # get the correct 3d model alignment transformation
    transform = du.get_3dm_alignment_to_frame(transformation_json, handover_keyframes, G_frame_index)
    print(f"transformation to align the 3D model to frame {G_frame_index}: {transform}")
    
    # apply the transform to the 3D model
    object_3dm.apply_transform(transform)
    print(f"object mesh {object_id} has been transformed")