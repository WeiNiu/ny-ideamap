#!/usr/bin/pythoni
# -*- coding: utf-8 -*-
import os, datetime, gzip, cjson, json
import fnmatch
import numpy as np
import operator
import string
import math
#from getTweets import GetTweets;
simplejson = json
import ast
#from tinysegmenter import *
from operator import itemgetter
import random

def centerTokens(dist_matrix, cluster_label):
    new_centroid = [];
    for center, tokens in cluster_label.iteritems():
        min_dist = 1111111;
        new_center = center;
        for token in tokens:
            total_dist = 0;
            for token2 in tokens:
                total_dist = total_dist + dist_matrix[token][token2];
            if total_dist < min_dist:
                min_dist = total_dist;
                new_center = token;
        new_centroid.append(new_center);

    return new_centroid;

def kmeansTokens(matrix, K):
    list = matrix.keys();
#    print list
    centroid = random.sample(list, K);
    label = {};
    dist = {};

    iter = 0;
    isChange = True;
    while iter < 200 and isChange:
        iter = iter + 1;
        # label the tokens
        cluster = {};
        for center in centroid:
            cluster[center] = [];

        for token in list:
            min_dis = 11111111;
            for center in centroid:
                if matrix[center][token] < min_dis:
                    min_dis = matrix[center][token];
                    sel_label = center;
            cluster[sel_label].append(token);

        # re-cal the centriod
        new_centroid = centerTokens(matrix, cluster);
        for center in new_centroid:
            if center not in centroid:
                isChange = True;
                break;
            isChange = False;
        centroid = new_centroid;

    return cluster;
dir='/home/wei/ideamap/reduced_tag_newyork/similarity2011_2_withuid_10-exp4'
filea=open(dir,'r')
matrix=eval(filea.readline())
#print matrix

output='./out10-exp4'
out=open(output,'w')
for i in range(2,20):
    cluster=kmeansTokens(matrix,i)
    print i
    print>>out, '--------------------'+str(i)+'----------------------'
    print>>out,cluster
