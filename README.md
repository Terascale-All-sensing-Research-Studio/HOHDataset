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


TODO:
- write documentation on missing_seg_ptcld.json and object_alignment_problems.json
