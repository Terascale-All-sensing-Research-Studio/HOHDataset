import os

import zipfile

import constants


def unzip_archive(zip_archive_path, extract_to):
    """
    Unzip the contents of a zip archive to a specified destination directory.

    Parameters:
    - zip_archive_path (str): Path of the zip archive.
    - extract_to (str): Destination directory for extracting contents.
    """
    with zipfile.ZipFile(zip_archive_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


if __name__ == "__main__":
    print(f"Unzipping data to: {constants.DATA_ROOTDIR}")
    input("Continue? Ctrl+C to quit.")

    DATA_TO_EXTRACT = [ os.path.join(constants.REPO_PATH, "data", f"HOH_Minimum_Datset{f}.zip") for f in [1,2,3] ] # for HOH Minimum Dataset
    DATA_TO_EXTRACT.extend([ os.path.join(constants.REPO_PATH, "data", f"HOH_Keyframe_Datset{f}.zip") for f in [1,2,3] ]) # for HOH Keyframe Dataset
    DATA_TO_EXTRACT.append(os.path.join(constants.REPO_PATH, "data", "full_116_and_120.zip")) # for HOH Objects
    DATA_TO_EXTRACT.append(os.path.join(constants.REPO_PATH, "data", "full.zip")) # for HOH Objects
    DATA_TO_EXTRACT.append(os.path.join(constants.REPO_PATH, "data", "watertight.zip")) # for HOH Objects
    DATA_TO_EXTRACT.append(os.path.join(constants.REPO_PATH, "data", "simplified.zip")) # for HOH Objects
    DATA_TO_EXTRACT.append(os.path.join(constants.REPO_PATH, "data", "simplified_2000.zip")) # for HOH Objects

    for i, p in enumerate(DATA_TO_EXTRACT):
        print(f"Extracting part {i} of {len(DATA_TO_EXTRACT)}... ")
        dest_p = constants.DATA_ROOTDIR
        if "HOH_" not in dest_p: # put objects in separate sub directory
            dest_p = os.path.join(dest_p, "HOH_Objects")
        os.makedirs(dest_p, exist_ok=True)
        try:
            unzip_archive(p, dest_p)
        except Exception as e:
            print("... not found. continuing. ")
            continue
        print("... complete!")
    
    
    print(f"All data unzipped to: {constants.DATA_ROOTDIR}")
