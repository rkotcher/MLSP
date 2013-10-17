from scipy.io import wavfile
import numpy as np

from sklearn import svm

# Read in a wav file, combine data into a numpy array with
# two columns by n rows
fs, mixed1 = wavfile.read("data/in/mixed1.wav")
fs, mixed2 = wavfile.read("data/in/mixed2.wav")

mixed1 = np.asarray([mixed1])
mixed2 = np.asarray([mixed2])

# Combine into, and transpose the mixture matrix
combined = np.concatenate((mixed1, mixed2), axis=0)
combined = combined.T

W,D = np.linalg.eig(np.dot(combined, combined.T));

# Write wav file to path
#wavfile.write("data/out/source1.wav", fs, sources[0])
#wavfile.write("data/out/source2.wav", fs, sources[1])
