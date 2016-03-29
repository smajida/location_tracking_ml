#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import pylab

import tensorflow as tf
from tensorflow.models.rnn import rnn, rnn_cell
import numpy as np
import scipy.io as sio

import random
import json
import itertools

# Saves .mat files for Octave
def save(file_name, variable_name, value):
    sio.savemat(file_name, {variable_name:value})

def export_to_octave(positionTracks):
    print('Creating Octave file.')
    pos = np.asarray(map(lambda l: list(l.itervalues()), positionTracks))
    sio.savemat('tracks.mat', {'pos': pos})
