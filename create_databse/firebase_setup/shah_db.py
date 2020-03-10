#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 03:38:37 2020

@author: kritverma
"""


import glob
import pickle
import json

shah_folder=glob.glob('../shah/pickle/*.pkl')
fb_json_file='../shah/timeline.json'



def create_db():
    shah={}
    shah['twitter']={}
    with open(fb_json_file) as f:
      fb_json = json.load(f)
    
    shah['facebook']=fb_json
    
    
    
    for i in shah_folder:
        file_name=i.split("/",3)[3]
        media_name=file_name.replace(".pkl","")
        data=pickle.load(open(i,'rb'))
        
        if(isinstance(data,list)):
            data_j=[]
            for j in data:
                data_j.append(j.__dict__['_json'])
            data_str=json.dumps(data_j)
            data_json=json.loads(data_str)
        elif(isinstance(data,dict)):
            data_json=data
        else:
            data_json=json.loads(data)
        
        if("json" in media_name):
            shah['scholar']=data_json
        elif("linkedin" in media_name):
            shah['linkedin']=data_json
        else:
            if('followers' in media_name):
                shah['twitter']['followers']=data_json
            elif('retweeters_freq' in media_name):
                shah['twitter']['retweeters_freq']=data_json
            elif('tweets' in media_name):
                shah['twitter']['tweets']=data_json
    return shah