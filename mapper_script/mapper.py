#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkContext,SparkConf
import numpy as np
from scipy import stats
import sys
import json
import re


# In[2]:


with open('sample_data.json',encoding='utf-8', errors='ignore') as json_data:
    data = json.load(json_data, strict=False)
outfile = open('final_data.json', 'w')
for k,v in data.items():
    final_data = {}
    final_data[k] = v
    json_object = json.dumps(final_data)
    outfile.write(json_object)
    outfile.write("\n")
outfile.close()


# In[3]:


conf = SparkConf()
sc = SparkContext(conf=conf)


# In[4]:


def map_1(data):
    data = json.loads(data)
    features = []
    for k,v in data.items():
        for key,val in v.items():
            if key == "country" or key =="country_code" or key == "food_availability_per_capita":
                continue
            else:
                features.append(float(val))
        features.append(float(v["food_availability_per_capita"]))
        return (v['country'],np.asarray(features))


# In[7]:


rdd = sc.textFile('final_data.json').map(map_1).groupByKey()


# In[8]:


rdd.take(2)

