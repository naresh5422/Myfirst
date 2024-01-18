import numpy as np
import pandas as pd
import os
import sys
from zipfile import ZipFile
from 

def data_extractor(zip_file):
    path = "Desktop/Myfirst"
    with ZipFile(zip_file, 'r') as zipdir:
        zipdir.extractall(path)
    return path


data_extractor("/home/cdot/Downloads/Face-Images.zip")