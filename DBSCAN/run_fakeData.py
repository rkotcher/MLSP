# Simple demo of a scatter plot.
# 
# Goal for today:
# 
#   Given::
#
#   X -> a set of points in 3 dimensional space (now, with a clear
#       division between classes. Draw them on paper first)
#   Y -> the classes (for now, either YES or NO)
# 
# Want to create an soft-margin SVM that can predict a new set of
# input points.

# A weird mac thing?? No idea really..
import pkg_resources
pkg_resources.require("matplotlib")

import pylab as pl
import matplotlib.font_manager

from support import *
from numpy import *
from sklearn.cluster import KMeans

DOG_LENGTH = 10
NOISE_LENGTH = 10
KMEANS_WINDOW_SIZE = 8

# "Dog bark" is changed around just a little bit each time and
# entered into the arrays. Assume that each array has at least one dog
# for now
dogA = random.random((1, DOG_LENGTH))
dogB = dogA + (random.random((1, DOG_LENGTH))/100)
dogC = dogA + (random.random((1, DOG_LENGTH))/100)
dogD = dogA + (random.random((1, DOG_LENGTH))/100)
dogE = dogA + (random.random((1, DOG_LENGTH))/100)

sourceA = concatenate([random.random((1, NOISE_LENGTH)), dogA, random.random((1, NOISE_LENGTH))], axis=1)
sourceB = concatenate([random.random((1, NOISE_LENGTH)), dogB, random.random((1, NOISE_LENGTH))], axis=1)
sourceC = concatenate([random.random((1, NOISE_LENGTH)), dogC, random.random((1, NOISE_LENGTH))], axis=1)
sourceD = concatenate([random.random((1, NOISE_LENGTH)), dogD, random.random((1, NOISE_LENGTH))], axis=1)
sourceE = concatenate([random.random((1, NOISE_LENGTH)), dogE, random.random((1, NOISE_LENGTH))], axis=1)

# Given a matrix of sources (same length) and window size, cluster the windows
# until at least one from each file is in some cluster
# vectors can be retrieved with sources[i]
sources = concatenate((sourceA, sourceB, sourceC, sourceD, sourceE))
prototypes = rdkMeans(sources, KMEANS_WINDOW_SIZE)

print "Prototypes:"
print prototypes

#print "Actual class of dogs:"
#print labels[NOISE_LENGTH]
#print labels[1*(2*NOISE_LENGTH + DOG_LENGTH - KMEANS_WINDOW_SIZE) + NOISE_LENGTH]
#print labels[2*(2*NOISE_LENGTH + DOG_LENGTH - KMEANS_WINDOW_SIZE) + NOISE_LENGTH]
#print labels[3*(2*NOISE_LENGTH + DOG_LENGTH - KMEANS_WINDOW_SIZE) + NOISE_LENGTH]
#print labels[4*(2*NOISE_LENGTH + DOG_LENGTH - KMEANS_WINDOW_SIZE) + NOISE_LENGTH]


#print kmeans.fit_predict()
#print kmeans.predict([1, 2])
#print kmeans.predict([11, 13])
#print kmeans.predict([12, 13])
#print kmeans.predict([9, 13])

