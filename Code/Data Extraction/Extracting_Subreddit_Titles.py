# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:36:54 2019

@author: bhara
"""
import pandas as pd
import requests
import json
import time
import datetime
import os
import json
from tqdm import tqdm_notebook as tqdm
import bz2
import re
import matplotlib.pyplot as plt

os.chdir('D:/UofT/CSC2552/Project_Proposal/Data/Sample Data')

subreddits_dat = pd.read_json("subreddits.json.gz",compression="gzip")