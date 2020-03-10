#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 01:12:48 2020

@author: kritverma
"""


import glob
import pickle
import json

darak_folder=glob.glob('../darak/pickle/*.pkl')
fb_json_file='../darak/timeline.json'

def remove_keys(json):
    for i,j in json.items():
        if(i=="" or i==[] or i=="$" or i=="#" or i=="/"):
            print(i)
            
def create_db():
    darak={}
    darak['twitter']={}
    
    
    with open(fb_json_file) as f:
      fb_json = json.load(f)
    
    darak['facebook']=fb_json
    
    
    
    for i in darak_folder:
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
            darak['scholar']=data_json
        elif("linkedin" in media_name):
            darak['linkedin']=data_json
        else:
            if('followers' in media_name):
                darak['twitter']['followers']=data_json
            elif('retweeters_freq' in media_name):
                darak['twitter']['retweeters_freq']=data_json
            elif('tweets' in media_name):
                darak['twitter']['tweets']=data_json
    return darak
       