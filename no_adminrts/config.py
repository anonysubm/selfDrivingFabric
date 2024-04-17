import random
from dotenv import load_dotenv
from itertools import product
import os

load_dotenv()


"""
=== GENERAL CONFIG ===
"""

#ALGORITHM = os.getenv("ALGORITHM")

# mongodb settings
#MONGODB_HOST = os.getenv("MONGODB_HOST")

# env config
#TEST_NETWORK_EXTENDED_DIR = os.getenv("TEST_NETWORK_EXTENDED_DIR")

# Tx duration in Hyperledger caliper
#TX_DURATION = 10 # caliper tx duration - TODO check with caliper config

# "reward vs penalty?, rather we can assign score for every agent action (changing configuration)"
MOVE_PENALTY = 1 
#THROUGHPUT_REWARD_WEIGHT = 1.5
#SUCCESS_REWARD_WEIGHT = 1
#LATENCY_REWARD_WEIGHT = 1.2

# if action picked is not possible to execute, give penalty
#INVALID_ACTION_PENALTY = 99

# if objective achieved, multiply reward by this value.
OBJECTIVE_REWARD_MULTIPLIER=5


# training config
EXPECTED_SUCCESSTHROUGHPUT = 1 # default expected throughput
MAXIMUM_STEPS_PER_EPISODE = 30
NUMBER_OF_EPISODES = 10
#MAXIMUM_STEPS_PER_EPISODE = 2
#NUMBER_OF_EPISODES = 4
LEARNING_RATE = 0.0003
LEARNING_STARTS = 3
EXPLORATION_FRACTION = 0.2
FIXED_THROUGHPUT = None


# notification config
#CHAT_ID = os.getenv("CHAT_ID")
#BOT_TOKEN = os.getenv("BOT_TOKEN")

# digital ocean spaces settings
#SPACE_KEY = os.getenv("SPACE_KEY")
#SPACE_SECRET = os.getenv("SPACE_SECRET")
#SPACE_NAME = os.getenv("SPACE_NAME")
#SPACE_REGION = os.getenv("SPACE_REGION")

# rebuild transaction limit
#REBUILD_LIMIT = 50000

"""
=== DQN CONFIG ===
"""
# possible value combination for action space (see PossibleAction)
max_message_count = [10,50,100,200,400]
preferred_max_bytes = [1,2,4,16]
batch_timeout = [0.5,1,2]
snapshot_interval_size = [16,32,64]
#admission_rate = [50,100,200,300]

#discrete_action_space = max_message_count
#discrete_action_space = list(product(max_message_count, preferred_max_bytes, batch_timeout, snapshot_interval_size, admission_rate))
discrete_action_space = list(product(max_message_count, preferred_max_bytes, batch_timeout, snapshot_interval_size))

#DQN_SIZE = 800 # max throughput TODO check with saturation_check.py

#SET_TPS = 100
#MIN_TPS = 50
#MAX_TPS = 300
#VAR_TPS = 50

#def get_tps_value():
    #SET_TPS = random.randrange(MIN_TPS, MAX_TPS, VAR_TPS) or 100
    #return SET_TPS

""" def set_dqn_expected_throughput(fixed_throughput):
    global EXPECTED_THROUGHPUT
    if fixed_throughput:
        EXPECTED_THROUGHPUT = fixed_throughput
    else:
        EXPECTED_THROUGHPUT = random.randrange(50, DQN_SIZE, 50) or 10
    return EXPECTED_THROUGHPUT """
