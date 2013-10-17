import wave, array

MAX_AUDIO_FRAMES = 100000

# (1) Data import
# Get the samples from each wave file
wavobject = wave.open('data/dog.wav', 'r')
samples = wavobject.readframes(MAX_AUDIO_FRAMES)

samplesAsFloats = array.array('B', samples)

print samplesAsFloats
