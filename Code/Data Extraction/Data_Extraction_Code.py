# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:21:12 2019

@author: bhara
"""

import pandas as pd
import requests
import json
import time
import datetime
import os
import json
import tqdm
import bz2
import re
import matplotlib.pyplot as plt
import pickle

bz_file = bz2.BZ2File('RS_2016-11.bz2')

subreddit_dict={"link_flair_text":[],"url":[],
                "id":[],"created_utc":[],"title":[],
                "author_flair_text":[],"author":[],
               "selftext":[],"domain":[],"num_comments":[],"subreddit_id":[],"score":[],"permalink":[],
               "subreddit":[]}

i=0
for line in bz_file:
    subreddit_json=json.loads(line.decode("utf-8"))
    if subreddit_json!=None and subreddit_json!={} :
    #and re.search(news_source,subreddit_json["url"])!=None:
        if(i%100000==0):
            print(i)
        i+=1
        
        if("subreddit_id" not in subreddit_json.keys()):
            continue
            
        subreddit_dict["link_flair_text"].append(subreddit_json["link_flair_text"])
        subreddit_dict["url"].append(subreddit_json["url"])
        subreddit_dict["id"].append(subreddit_json["id"])
        subreddit_dict["created_utc"].append(subreddit_json["created_utc"])
        subreddit_dict["permalink"].append(subreddit_json["permalink"])
        subreddit_dict["subreddit"].append(subreddit_json["subreddit"])
        subreddit_dict["title"].append(subreddit_json["title"])
        subreddit_dict["author_flair_text"].append(subreddit_json["author_flair_text"])
        subreddit_dict["author"].append(subreddit_json["author"])
        subreddit_dict["selftext"].append(subreddit_json["selftext"])
        subreddit_dict["domain"].append(subreddit_json["domain"])
        subreddit_dict["num_comments"].append(subreddit_json["num_comments"])
        subreddit_dict["subreddit_id"].append(subreddit_json["subreddit_id"])
        subreddit_dict["score"].append(subreddit_json["score"])
        
with open('Submissions_Nov2016.pickle', 'wb') as handle:
    pickle.dump(subreddit_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)