import random
from dotenv import load_dotenv
from itertools import product
import os
from sklearn import preprocessing

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
MAXIMUM_STEPS_PER_EPISODE = 300
NUMBER_OF_EPISODES = 3

#LEARNING_RATE = 0.0003
LEARNING_RATE = 0.0001
EXPLORATION_FRACTION = 0.2
FIXED_THROUGHPUT = None

LEARNING_STARTS = 100
BUFFER_SIZE = 10000
BATCH_SIZE = 64
PRIORITIZED_REPLAY = True
NETWORK_UPDATE_FREQUENCY = 1000


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

#Number of clients 10
client_1 = [0.5,0,1]
client_2 = [0.5,0,1]
client_3 = [0.5,0,1]
client_4 = [0.5,0,1]
client_5 = [0.5,0,1]
client_6 = [0.5,0,1]
client_7 = [0.5,0,1]
client_8 = [0.5,0,1]
client_9 = [0.5,0,1]
client_10 = [0.5,0,1]

# # possible value combination for action space (see PossibleAction)
# real_max_message_count = [100,300,500]
# real_preferred_max_bytes = [2,4,16]
# real_batch_timeout = [0.5,1,2]
# real_snapshot_interval_size = [16,32,64]

# #normalized action space
# max_message_count = (preprocessing.normalize([real_max_message_count]))[0].tolist()
# preferred_max_bytes = (preprocessing.normalize([real_preferred_max_bytes]))[0].tolist()
# batch_timeout = (preprocessing.normalize([real_batch_timeout]))[0].tolist()
# snapshot_interval_size = (preprocessing.normalize([real_snapshot_interval_size]))[0].tolist()

#max_message_count = [0.16903085094570333, 0.50709255283711, 0.8451542547285166]
#preferred_max_bytes = [0.1203858530857692, 0.2407717061715384, 0.9630868246861536]
#batch_timeout = [0.2182178902359924, 0.4364357804719848, 0.8728715609439696]
#snapshot_interval_size = [0.2182178902359924, 0.4364357804719848, 0.8728715609439696]

# max_message_count = normalize(real_max_message_count, range_to_normalize[0], range_to_normalize[1])
# preferred_max_bytes = normalize(real_preferred_max_bytes, range_to_normalize[0], range_to_normalize[1])
# batch_timeout = normalize(real_batch_timeout, range_to_normalize[0], range_to_normalize[1])
# snapshot_interval_size = normalize(real_snapshot_interval_size, range_to_normalize[0], range_to_normalize[1])
#admission_rate = [50,100,200,300]

#discrete_action_space = max_message_count
#discrete_action_space = list(product(max_message_count, preferred_max_bytes, batch_timeout, snapshot_interval_size, admission_rate))
discrete_action_space = list(product(client_1, client_2, client_3, client_4, client_5, client_6, client_7, client_8, client_9, client_10))

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
