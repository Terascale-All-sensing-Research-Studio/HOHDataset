import os

"""
This file contains various global reference information for path construction and data management.
"""

# path-related variables
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_ROOTDIR = os.path.join(REPO_PATH, "data", "HOH") # the root directory of the extracted HOH data

METADATA_PATH = os.path.join(DATA_ROOTDIR, "{}/reference/{}.json") #.format(capture_dir, capture_dir)
SEGMENTED_POINTCLOUD_PATH = os.path.join(DATA_ROOTDIR, "{}/PCFiltered/{}/{}_frame{}.ply") #.format(capture_dir, handover_idx, target, frame_idx)
SCENE_POINTCLOUD_PATH = os.path.join(DATA_ROOTDIR, "{}/PCFull/{}/frame{}.ply") #.format(capture_dir, handover_idx, frame_idx) 
THREEDM_ALIGNMENTS_PATH = os.path.join(DATA_ROOTDIR, "{}/3dModelAlignments/{}_{}_transformations.json") #.format(capture_dir, capture_dir, handover_idx)
KCOLOR_IMAGE_PATH = os.path.join(DATA_ROOTDIR, "{}/Azure/{}/{}/cam{}_frame{}.png") #.format(capture_dir, handover_idx, cam_idx, cam_idx, frame_idx)
KCOLOR_MASK_PATH = os.path.join(DATA_ROOTDIR, "{}/MaskTracking/{}/{}/{}_mask_frame{}_cam{}.npz") #.format(capture_dir, handover_idx, cam_idx, target, frame_idx, cam_idx)
OPENPOSE_SKELETON_PATH = os.path.join(DATA_ROOTDIR, "{}/OpenPose/{}/{}/frame{}_cam{}_keypoints.json") #.format(capture_dir, handover_idx, cam_idx, frame_idx, cam_idx)
OBJECT_MODEL_PATH = os.path.join(DATA_ROOTDIR, "HOH_Objects/{}/{}_{}.obj") #.format(model_type, object_id, model_type)
OBJECT_116_PATH = os.path.join(DATA_ROOTDIR, "116/VASE_CLMS_V002-2.stl") # object 116 only
OBJECT_120_PATH = os.path.join(DATA_ROOTDIR, "120/Baby_Yoda.obj") # object 120 only

# data constants
KCOLOR_HW = (1080, 1920) # pixel height and width of Kinect color images
DEPTH_HW = (576, 640) # pixel height and width of Kinect depth images

# openpose joint definitions
JOINT_PAIRS_MAP_ALL = {(0, 15):  {'joint_names': ('Nose', 'REye')},
                       (0, 16):  {'joint_names': ('Nose', 'LEye')},
                       (1, 0):   {'joint_names': ('Neck', 'Nose')},
                       (1, 2):   {'joint_names': ('Neck', 'RShoulder')},
                       (1, 5):   {'joint_names': ('Neck', 'LShoulder')},
                       (1, 8):   {'joint_names': ('Neck', 'MidHip')},
                       (2, 3):   {'joint_names': ('RShoulder', 'RElbow')},
                    #    (2, 17): {'joint_names': ('RShoulder', 'REar')},
                       (3, 4):   {'joint_names': ('RElbow', 'RWrist')},
                       (5, 6):   {'joint_names': ('LShoulder', 'LElbow')},
                    #    (5, 18): {'joint_names': ('LShoulder', 'LEar')},
                       (6, 7):   {'joint_names': ('LElbow', 'LWrist')},
                       (8, 9):   {'joint_names': ('MidHip', 'RHip')},
                       (8, 12):  {'joint_names': ('MidHip', 'LHip')},
                       (9, 10):  {'joint_names': ('RHip', 'RKnee')},
                       (10, 11): {'joint_names': ('RKnee', 'RAnkle')},
                       (11, 22): {'joint_names': ('RAnkle', 'RBigToe')},
                       (11, 24): {'joint_names': ('RAnkle', 'RHeel')},
                       (12, 13): {'joint_names': ('LHip', 'LKnee')},
                       (13, 14): {'joint_names': ('LKnee', 'LAnkle')},
                       (14, 19): {'joint_names': ('LAnkle', 'LBigToe')},
                       (14, 21): {'joint_names': ('LAnkle', 'LHeel')},
                       (15, 17): {'joint_names': ('REye', 'REar')},
                       (16, 18): {'joint_names': ('LEye', 'LEar')},
                       (19, 20): {'joint_names': ('LBigToe', 'LSmallToe')},
                       (22, 23): {'joint_names': ('RBigToe', 'RSmallToe')}}