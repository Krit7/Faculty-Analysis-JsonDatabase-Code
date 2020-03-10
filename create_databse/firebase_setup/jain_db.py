#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 03:38:48 2020

@author: kritverma
"""


import glob
import pickle
import json

jain_folder=glob.glob('../jain/pickle/*.pkl')
fb_json_file='../jain/timeline.json'


def create_db():
    jain={}
    jain['twitter']={}
    
    
    with open(fb_json_file) as f:
      fb_json = json.load(f)
    
    jain['facebook']=fb_json
    
    
    
    for i in jain_folder:
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
            jain['scholar']=data_json
        elif("linkedin" in media_name):
            jain['linkedin']=data_json
        else:
            if('followers' in media_name):
                jain['twitter']['followers']=data_json
            elif('retweeters_freq' in media_name):
                jain['twitter']['retweeters_freq']=data_json
            elif('tweets' in media_name):
                jain['twitter']['tweets']=data_json
    return jain
            