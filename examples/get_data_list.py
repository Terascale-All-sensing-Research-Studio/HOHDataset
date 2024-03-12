import sys 

sys.path.append("../")
import constants
import data_utils as du

"""
This file contains an example of how to retrieve a list of all
capture directories and all samples in the HOH dataset.
"""


if __name__ == "__main__":

    # retrieve global list of all capture directories
    capture_dirs = constants.capture_dirs
    print("The HOH Dataset contains {} capture_dirs. The first is: {}".format(len(capture_dirs), capture_dirs[0]))

    all_samples = du.all_samples()
    print("The HOH Dataset contains {} handover interactions. The first is: {}".format(len(all_samples), all_samples[0]))
