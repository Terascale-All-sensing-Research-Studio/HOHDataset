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
SYNC_LUT_PATH = os.path.join(DATA_ROOTDIR, "Sync_Info", "{}_azure_lightsync_lut.txt") #.format(capture_dir)
RAW_IMAGES_PATH = os.path.join(DATA_ROOTDIR, "{}/Azure/{}/{}") #.format(capture_dir, camera_name, image_name)
RAW_KCOLOR_MASK_PATH = os.path.join(DATA_ROOTDIR, "{}/MaskTracking/MaskTracking/{}/{}_{}_masks.npz") #.format(capture_dir, cam_idx, target, handover_idx)
RAW_KCOLOR_OBJECT_ONLY_MASK_PATH = os.path.join(DATA_ROOTDIR, "{}/MaskTracking/MaskTracking/{}/object_only_{}_mask.npz") #.format(capture_dir, cam_idx, handover_idx)
RAW_OPENPOSE_SKELETON_PATH = os.path.join(DATA_ROOTDIR, "{}/OpenPose/{}/{}_cam{}_keypoints.json") #.format(capture_dir, handover_idx, frame_idx, cam_idx)
RAW_SCENE_POINTCLOUD_PATH = os.path.join(DATA_ROOTDIR, "{}/PCFull/full/{}/full_kcolor_frame{}.ply") #.format(capture_dir, handover_idx, frame_idx)
COLOR_IMAGE_NAME = "azurecolor-{}.jpg" #.format(timestamp)
DEPTH_IMAGE_NAME = "azuredepth-{}.jpg" #.format(timestamp)
CAM_NAMES = ["PROCESSED__0_000162504612", "PROCESSED__1_000053604612", "PROCESSED__2_000036504612", "PROCESSED__3_000372200712"] # name constants for image directories

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

# all 178 capture directory names
capture_dirs = ["01638-46157-S1", "01638-46157-S16", "01638-46157-S32", "01638-46157-S50", "01638-46157-S60", "02781-96731-S1", "02781-96731-S18", "02781-96731-S35", 
                "02781-96731-S52", "04752-09631-S1", "04752-09631-S18", "04752-09631-S35", "04752-09631-S52", "04921-12586-S1", "04921-12586-S16", "04921-12586-S32", 
                "04921-12586-S33", "04921-12586-S50", "04921-12586-S65", "07326-87510-S1", "07326-87510-S18", "07326-87510-S33", "07326-87510-S51", "09631-04752-S1", 
                "09631-04752-S18", "09631-04752-S35", "09631-04752-S52", "12586-04921-S1", "12586-04921-S16", "12586-04921-S30", "12586-04921-S33", "12586-04921-S52", 
                "12586-04921-S53", "12634-49260-S1", "12634-49260-S15", "12634-49260-S31", "12634-49260-S45", "12634-49260-S58", "13026-17623-S1", "13026-17623-S18", 
                "13026-17623-S35", "13026-17623-S52", "17623-13026-S1", "17623-13026-S18", "17623-13026-S35", "17623-13026-S52", "19860-57643-S1", "19860-57643-S18", 
                "19860-57643-S35", "19860-57643-S52", "26718-29401-S1", "26718-29401-S18", "26718-29401-S33", "26718-29401-S52", "29401-26718-S1", "29401-26718-S22", 
                "29401-26718-S43", "36817-46823-S1", "36817-46823-S18", "36817-46823-S35", "36817-46823-S52", "42679-65094-S1", "42679-65094-S16", "42679-65094-S31", 
                "42679-65094-S46", "42679-65094-S65", "43017-98754-S1", "43017-98754-S18", "43017-98754-S31", "43017-98754-S50", "43017-98754-S68", "46157-01638-S1", 
                "46157-01638-S16", "46157-01638-S31", "46157-01638-S49", "46157-01638-S54", "46823-36817-S1", "46823-36817-S18", "46823-36817-S32", "46823-36817-S48", 
                "46823-36817-S64", "49260-12634-S1", "49260-12634-S18", "49260-12634-S3", "49260-12634-S34", "49260-12634-S51", "50269-85603-S1", "50269-85603-S15", 
                "50269-85603-S31", "50269-85603-S50", "53978-82931-S1", "53978-82931-S18", "53978-82931-S35", "53978-82931-S52", "57643-19860-S1", "57643-19860-S18", 
                "57643-19860-S35", "57643-19860-S52", "59810-86132-S1", "59810-86132-S16", "59810-86132-S28", "59810-86132-S43", "59810-86132-S56", "60514-65807-S1", 
                "60514-65807-S20", "60514-65807-S3", "60514-65807-S38", "60514-65807-S56", "61205-79132-S1", "61205-79132-S17", "61205-79132-S34", "61205-79132-S52", 
                "64098-79325-S1", "64098-79325-S18", "64098-79325-S35", "64098-79325-S52", "65094-42679-S1", "65094-42679-S13", "65094-42679-S29", "65094-42679-S48", 
                "65807-60514-S1", "65807-60514-S18", "65807-60514-S2", "65807-60514-S35", "65807-60514-S52", "79132-61205-S1", "79132-61205-S18", "79132-61205-S35", 
                "79132-61205-S52", "79325-64098-S1", "79325-64098-S18", "79325-64098-S35", "79325-64098-S52", "82367-86732-S1", "82367-86732-S18", "82367-86732-S28", 
                "82367-86732-S45", "82367-86732-S62", "82931-53978-S1", "82931-53978-S18", "82931-53978-S34", "82931-53978-S51", "82931-53978-S55", "85603-50269-S1", 
                "85603-50269-S18", "85603-50269-S35", "85603-50269-S51", "86132-59810-S1", "86132-59810-S18", "86132-59810-S32", "86132-59810-S50", "86132-59810-S64", 
                "86732-82367-S1", "86732-82367-S18", "86732-82367-S29", "86732-82367-S46", "86732-82367-S63", "87510-07326-S1", "87510-07326-S17", "87510-07326-S34", 
                "87510-07326-S51", "96731-02781-S1", "96731-02781-S18", "96731-02781-S35", "96731-02781-S52", "98754-43017-S1", "98754-43017-S14", "98754-43017-S24", 
                "98754-43017-S44", "98754-43017-S64", "65928-82756-S1", "65928-82756-S18", "65928-82756-S35", "65928-82756-S52", "82756-65928-S1", "82756-65928-S18", 
                "82756-65928-S35", "82756-65928-S52"]