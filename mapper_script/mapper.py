#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkContext, SparkConf
import numpy as np
from scipy import stats
import sys
import json
import re
import tensorflow as tf



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


# implement multiple linear regression
def mlinreg(data):
    # convert list of np arrays into a single array
    myarray = np.vstack(data)
    print('size of input matrix: ' + str(myarray.size))

    # the number of dependent variables
    n = myarray[0].size - 1

    # dependent variables
    # pick first n columns into deps and transpose it
    # deps' dimension is n*m (m is the number of data points in each record)
    deps = myarray[:, 0:n].transpose()

    # independent variable
    # pick the last column into indeps and transpose it
    # indeps' dimension is 1*m
    indeps = myarray[:, n].transpose()

    # mean and std dev of deps and indeps
    mean_deps = np.mean(deps, axis = 1)
    mean_indeps = np.mean(indeps, axis = 1)
    sd_deps = np.std(deps, axis = 1)
    sd_indeps = np.std(indeps, axis = 1)

    # standardize deps and indeps
    temp_list = []
    for i in range(deps.size):
        temp_list.append([(elem - mean_deps[i])/sd_deps[i] for elem in deps[i]])
    std_deps = np.array(temp_list)

    temp_list = []
    for i in range(indeps.size):
        temp_list.append((indeps[i] - mean_indeps)/sd_indeps)
    std_indeps = np.array(temp_list)

    # initialize beta and bias(b)
    beta = tf.get_variable("beta", shape=(1, n))
    b = tf.get_variable("b", shape=())

    X = tf.placeholder(tf.float32, shape=(n, None))
    Y = tf.placeholder(tf.float32, shape=(1, None))

    # calculate predicted value
    Y_pred = tf.matmul(beta, X) + b

    # loss function
    l = tf.reduce_sum((Y_pred - Y)**2)

    # initialize optimizer
    opt = tf.train.AdamOptimizer(learning_rate=0.1).minimize(l)

    # Create a tf session
    session = tf.Session()
    session.run(tf.global_variables_initializer())

    # optimization loop
    for i in range(20):
        _, c_l, c_beta, c_b = session.run([opt, l, beta, b], feed_dict={
            X: std_deps,
            Y: std_indeps
    })
    print("loop# = %g, loss = %g, beta = %s, b = %g" % (i, c_l, str(c_beta), c_b))

    # T-test
    # degree of freedom
    df = myarray.size - (n + 1)

    # calculate std error of beta
    rss = np.sum((std_indeps - tf.matmul(beta, std_deps))**2)
    sSquared = rss / df
    se = []
    t_stat = []
    p = []
    for i in range(n):
        se.append(np.sqrt(sSquared/np.sum([((elem - mean_deps[i]) ** 2) for elem in deps[i]])))

    # t statistic
    for i in range(n):
        t_stat.append((c_beta[i]/se[i]))

    # p value
    for i in range(n):
        p.append(stats.t.sf(np.abs(t_stat[i]), df))

    # obtain the index of the smallest p value in p
    ind = np.argpartition(p, 1)

    if p < 0.05/1032:
        return ind[:1]
    else:
        return ['no significant crop']





rdd.mapValues(mlinreg)

