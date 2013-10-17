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
#   ^ Finished the above task. The next goal is to make an API for
#   rdkDBSCAN, that is easy to use. Then test it on larger files
#   downloaded from youtube.
#
#
#   Next steps::
#   
#   If things seem to be working on manually created datasets, test
#   the rdkDBSCAN API on real youtube data.
#
#   created by rdk on 10-14-13

# A weird mac thing?? No idea really.. If you're running a mac, you'll
# want to leave this in here.
import pkg_resources
pkg_resources.require("matplotlib")
# END weird mac thing

#import itertools

# These imports are the python standard libraries for scientific
# computing. If you don't have them, see the installation instructions
# in INSTALL
import scipy
from numpy import *
from scipy.io import wavfile

# Things I've written.
# rdkDBSCAN: the API for easily running DBSCAN on large multimedia
# datasets
# latte: a library of support functions for this project.
from latte import *
from dbscan import rdkDBSCAN

# TODO put this into a config file
WINDOW_SIZE     = 44100
WINDOW_OVERLAP  = WINDOW_SIZE
NUM_CHANNELS    = 1

# TODO Fix this to read all files in a directory
# Load in data points from wav files, for now trim them to all be
# the length of the shortest file
fs, sample1 = wavfile.read("data/in/sample1.wav")
fs, sample2 = wavfile.read("data/in/sample2.wav")
fs, sample3 = wavfile.read("data/in/sample3.wav")

sample1   = trimData(sample1, WINDOW_SIZE, NUM_CHANNELS)
sample2   = trimData(sample2, WINDOW_SIZE, NUM_CHANNELS)
sample3   = trimData(sample3, WINDOW_SIZE, NUM_CHANNELS)

samples1  = datify(sample1, WINDOW_SIZE, WINDOW_OVERLAP)
samples2  = datify(sample2, WINDOW_SIZE, WINDOW_OVERLAP)
samples3  = datify(sample3, WINDOW_SIZE, WINDOW_OVERLAP)

samples = vstack((samples1, samples2, samples3))



# Run dbscan on this data, and get prototypes
prototypes = rdkDBSCAN(samples, WINDOW_SIZE)

#print "Summary: Got ", len(prototypes), " prototypes"
#print "\nEach has ", len(prototypes[0]), " samples"

#wavfile.write("data/out/results.wav", fs, array(list(itertools.chain.from_iterable(prototypes))))
