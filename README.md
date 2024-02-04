# HOH Dataset Variants Available

# HOH Keyframe Dataset
This is a version of HOH that includes data for the O, G, T, and R keyframes as defined in the HOH paper. Data included:
- Kinect Color images (all cameras)
- Object, Giver Hand, Receiver Hand segmentation masks, corresponding to color images
- OpenPose skeletons for each participant, corresponding to color images
- Full scene point clouds with background curtains removed
- Object 3D model alignment transformations
- Per-capture metadata, including keyframe indices, comfort ratings, object information, etc.

# HOH Minimum Dataset
This is a version of the dataset that includes data for all frames (including keyframes). Data included:
- Filtered point clouds isolating the Object, Giver Hand, and Receiver Hand
- Object 3D model alignment transformations
- Per-capture metadata
- All other metadata related to participant responses and demographics

# HOH Object Dataset
This is a version of the dataset that includes all object-related data, including:
- All object 3D models
  - Full resolution ("*_cleaned.obj")
  - Watertight ("*_watertight.obj")
  - Simplified (to approximately 10,000 vertices) ("*_simplified.obj")
  - Simplified_2000 (to approximately 2,000 vertices) ("*_simplified_2000.obj")
- All object metadata ("Metadata_HOH.csv")

Please visit the project page for more information and access to the mentioned dataset variants: https://hohdataset.github.io/
Additionally, please look at the `examples` directory for code demonstrations on how to use various components of the data.

NOTE: File `missing_segmented_pointcloud.json` contains a list of known missing segmented point clouds. Point clouds may be missing due to 
      the frame being dropped during recording or significant failure during tracking. Access this list by loading the json file, accessing
      the key "files", and selecting an entry in the list. Each list entry is a dict containing the handover ("sample"), the frame index ("frame_idx"),
      and the target ("target") that is missing.
