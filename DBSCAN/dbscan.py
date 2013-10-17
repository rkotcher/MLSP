from numpy import *
from sklearn.cluster import DBSCAN

# rdkMeans
#
# using window size 'windowSize', collects all possible sources from
# sources and clusters with different sizes until a cluster contains
# a sample from every class
def rdkDBSCAN(X, windowSize):

  #### TODO just for testing #####
  #X = []
  #for i in range(0, len(X)):


  #
  # run dbscan
  #
  curr_eps = 100000.0
  db = DBSCAN(eps=curr_eps, min_samples=3).fit(X) 
  
  labels = db.labels_
  max_value = max(labels)
  while max_value < 0:
    print curr_eps
    curr_eps = curr_eps + 50
    db = DBSCAN(eps=curr_eps, min_samples=3).fit(X) 
    max_value = max(db.labels_)

  #
  # get prototypes
  #
  labels = db.labels_
  prototypes = []
  for i in range(0, int(max_value) + 1):
    for j in range(0, len(labels)):
      if labels[j] == i:
        # Found another prototype
        #source_number = int(floor(j / NUM_LABELS_PER_SOURCE))
        #print source_number
        #start_index = j % NUM_LABELS_PER_SOURCE
        #stop_index = start_index + windowSize 
        #n_prototype = [sources[source_number, start_index:stop_index]]
        #prototypes = prototypes + n_prototype
        prototypes = prototypes + X[j]
  
  print prototypes

  return prototypes
