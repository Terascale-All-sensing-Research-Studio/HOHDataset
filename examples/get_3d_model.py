import os 
import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to determine which object was
used for a particular handover using the metadata. Additionally, 
this file demonstrates how to load the 3D model for this object.
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
   
    
