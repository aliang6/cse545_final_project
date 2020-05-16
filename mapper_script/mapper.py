#!/usr/bin/env python
# coding: utf-8

import csv
# In[1]:
import functools
import io
import json

import numpy as np
import tensorflow as tf
from pyspark import SparkContext, SparkConf
from scipy import stats

# In[2]:


with open('sample_data.txt', encoding='utf-8', errors='ignore') as json_data:
    data = json.load(json_data, strict=False)
outfile = open('final_data.json', 'w')
for k, v in data.items():
    final_data = {k: v}
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
    for k, v in data.items():
        for key, val in v.items():
            if key == "country" or key =="country_code" or key == "food_availability_per_capita":
                continue
            else:
                features.append(float(val))
        features.append(float(v["food_availability_per_capita"]))
        return (v['country'], np.asarray(features))


# In[7]:


rdd = sc.textFile('final_data.json').map(map_1).groupByKey()  # mapValues(list).collect()


# In[8]:
rdd.take(2)


def f_batch_tensorflow(beta, A, B):
    # calculate predicted value
    e = tf.matmul(beta, A) - B

    # return loss
    return tf.reduce_sum(tf.square(e))


# implement multiple linear regression
def mlinreg(data):
    # convert list of np arrays into a single array
    myarray = np.vstack(data)
    print('size of input matrix: ' + str(np.size(myarray, 0)))

    # the total number of dependent variables and independent variables
    n = np.size(myarray, 1)

    # dependent variables
    # pick first n columns into deps and transpose it
    # deps' dimension is n*m (m is the number of data points in each record)
    indeps1 = np.hstack((np.ones((np.size(myarray, 0), 1)), myarray[:, 0:n-1])).transpose()

    # independent variable
    # pick the last column into indeps and transpose it
    # indeps' dimension is 1*m
    deps1 = myarray[:, n-1].transpose()

    # mean and std dev of deps and indeps
    mean_indeps1 = np.mean(indeps1, axis = 1)
    sd_indeps1 = np.std(indeps1, axis = 1)

    # standardize indeps
    temp_list = []
    for i in range(np.size(indeps1, 0)):
        # do something different with all-zero rows in a sparse matrix
        if np.sum(indeps1[i]) != 0 and sd_indeps1[i] == 0:
            temp_list.append([(elem - mean_indeps1[i]) / np.finfo(float).eps for elem in indeps1[i]])
        elif np.sum(indeps1[i]) != 0 and sd_indeps1[i] != 0:
            temp_list.append([(elem - mean_indeps1[i]) / sd_indeps1[i] for elem in indeps1[i]])
        else:
            temp_list.append(indeps1[i])

    std_indeps1 = np.asarray(temp_list)
    std_deps1 = np.asarray(deps1)

    X = tf.constant(indeps1)
    Y = tf.constant(deps1)

    # initialize beta(first element is bias)
    beta = tf.Variable(np.random.randn(1, n))

    f_without_any_args = functools.partial(f_batch_tensorflow, beta=beta, A=X, B=Y)
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
    optimizer.minimize(f_without_any_args, beta)
    print(optimizer)

    # T-test
    # degree of freedom
    df = np.size(myarray, 0) - n

    # calculate std error of beta
    rss = tf.reduce_sum(tf.square(std_deps1 - tf.matmul(beta, std_indeps1)))
    sSquared = rss / df
    se = []
    t_stat = []
    p = []
    for i in range(1, np.size(indeps1, 0)):
        npsum = np.sum([((elem - mean_indeps1[i]) ** 2) for elem in indeps1[i]])

        if np.sum(indeps1[i]) != 0 and npsum != 0:
            se.append(np.sqrt(sSquared/npsum))
        elif np.sum(indeps1[i]) != 0 and npsum == 0:
            se.append(np.sqrt(sSquared/np.finfo(float).eps))
        else:
            se.append(np.finfo(float).eps)

    beta_flat = np.asarray([elem for elem in beta[0]])
    se = np.asarray(se)
    # t statistic
    t_stat = tf.divide(beta_flat[1:n], se)

    # p value
    for i in range(0, np.size(indeps1, 0)-1):
        p.append(stats.t.sf(np.abs(t_stat[i]), df))

    # obtain the index of the smallest p value in p
    if min(p) < 0.05/(n-1):
        return p.index(min(p))
    else:
        return [str(df) + 'no significant crop']


def list_to_csv_str(row):
    output = io.StringIO('')
    csv.writer(output).writerow(row)
    return output.getvalue().strip()


rdd = rdd.mapValues(mlinreg)
# rdd = rdd.map(list_to_csv_str)
# rdd.saveAsTextFile('output.csv')  # could be your local directory
