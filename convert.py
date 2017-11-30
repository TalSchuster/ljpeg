import ljpeg
import math
import numpy as np
import os

path_to_ddsm = "/scratch1/tmansour/figment.csee.usf.edu/pub/DDSM/cases/"

for root, subFolders, file_names in os.walk(path_to_ddsm):
    for file_name in file_names:
        if ".LJPEG" in file_name:
            print(file_name)
            ljpeg_path = os.path.join(root, file_name)
            out_path = os.path.join(root, file_name)
            out_path = out_path.split('.LJPEG')[0] + ".tiff"

            cmd = './ljpeg.py "{0}" "{1}"'.format(ljpeg_path, out_path)
            os.system(cmd)

print('done')
