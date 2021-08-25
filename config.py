import os
import json
import time
import re
import shutil
import traceback

# FLAGS
USE_MULTIPROCESSING = False

# Directories
BASE_DIR = os.path.dirname(__file__)

FRAME_DIM = (352, 288, 3)

FRAME_RATE = 30

AUDIO_RATE = 44100

AUDIO_DEPTH = 2

DB_VID_ROOT = os.path.join(BASE_DIR, 'database')
QUERY_VID_ROOT = os.path.join(BASE_DIR, 'query')

BM_MACROBLOCK_SIZE = 16
BM_DISTANCE = 5

FEATURE_WEIGHTS = {
    'brightness_profile_y': 0.04,
    'brightness_profile_r': 0.02,
    'brightness_profile_g': 0.02,
    'brightness_profile_b': 0.02,
    'perceptual_hash_ahash': 0.02,
    'perceptual_hash_phash': 0.02,
    'perceptual_hash_whash': 0.02,
    'perceptual_hash_dhhash': 0.02,
    'perceptual_hash_dvhash': 0.02,
    'blockmotion_vecs_x': 0.2,
    'blockmotion_vecs_y': 0.1,
    'audio_spectral_profile': 0.5,
}

FEATURE_COLORS = {
    'brightness_profile_y': 'darkgrey', #'#7f7f7f',
    'brightness_profile_r': 'red', #'#ff0000',
    'brightness_profile_g': 'green', #'#00ff00',
    'brightness_profile_b': 'blue', #'#0000ff',
    'perceptual_hash_ahash': 'mediumslateblue', #'#7f7f00',
    'perceptual_hash_phash': 'mediumpurple', #'#ffff00',
    'perceptual_hash_whash': 'rebeccapurple', #'#3f3f00',
    'perceptual_hash_dhhash': 'indigo', #'#373700',
    'perceptual_hash_dvhash': 'darkorchid', #'#777700',
    'blockmotion_vecs_x': 'steelblue', #'#00ffff',
    'blockmotion_vecs_y': 'olivedrab', #'#007f7f',
    'audio_spectral_profile': 'gold', #'#ff00ff',
}

DEFAULT_WEIGHT = 0

# Loading local settings
#   To create a local configuration and add local overrides to these settings, make a local_config.py and override any setting values.
#   Do not add any additional settings in local_config.py. All settings in local_config must also appear in config.py
if os.path.exists(os.path.join(BASE_DIR, 'local_config.py')):
    print("Loading local configuration and overriding base settings")
    exec(open(os.path.join(BASE_DIR, 'local_config.py'), 'r').read())
else:
    print("No local configuration files found")
