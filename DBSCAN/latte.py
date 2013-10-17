# latte.py - my supporter methods
#
#
# Description::
# A set of supporter methods for working with scipy wav data and
# numpy array data types
#
# Dependencies:
# import numpy
# import scipy.io
#
# Methods:
# - trimData: makes data equal 0 mod windowSize
#

from numpy import *

# trimData: makes data equal to 0 mod windowSize
#   @param data - the data to trim
#   @param windowSize - the size you'll be using in your algo
def trimData(data, windowSize, numChannels):
  print "warning: trimData is ignoring the numChannels parameter"
  
  dataLength = len(data)
  numWindowsToKeep = int( dataLength / windowSize ) * windowSize;
  
  dataAsRowVectors = data[0:numWindowsToKeep].T[0]
  return dataAsRowVectors

# datify: converts an <np.array(...)> into a matrix of samples of
#         length windowSize with overlap overlapping samples. Assumes
#         the array is a row vector
#   @param windowSize - the size of the windows returned
#   @param overlap - number of samples until the next window
#
#   @returns - an <n x m> matrix, where each row is a new data sample
#
# NOTE the method isn't optimal. It may drop a few samples at the end
# of a vector, but not enough to spend valuable time on right now
def datify(data, windowSize, overlap):
  assert len(data) % windowSize == 0

  npArrayBuffer = None # an empty buffer to load data into
  for i in range(0, len(data) - windowSize):
    if i % overlap == 0:
      if npArrayBuffer == None:
        npArrayBuffer = array([data[i:i+windowSize]])
      elif i+windowSize < len(data) - 1:
        npArrayBuffer = concatenate((npArrayBuffer, array([data[i:i+windowSize]])), axis=0)

  return npArrayBuffer

