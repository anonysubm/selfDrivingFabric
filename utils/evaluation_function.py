"""
from the paper
evaluation function is using reward function
"""

import config
from config import MOVE_PENALTY

def relative_successthroughput_reward(curr_state):
    #return (round(curr_state[0] + (curr_state[5] / 1000), 2))
    #return (round(((curr_state[0] * curr_state[5]) / 500), 2))
    return (round((curr_state[0] / curr_state[1]), 2))  #throughput/sendrate
    #return (round((curr_state[0] / curr_state[1]), 2))  #succthroughput/sendrate

# def throughput_reward(curr_state, next_state):
#     return (next_state[0] - curr_state[0]) * THROUGHPUT_REWARD_WEIGHT


# def latency_reward(curr_state, next_state):
#     return (curr_state[2] - next_state[2]) * LATENCY_REWARD_WEIGHT


# def success_reward(curr_state, next_state):
#     return (next_state[1] - curr_state[1]) * SUCCESS_REWARD_WEIGHT


def penalty(curr_state, next_state):
    return MOVE_PENALTY


# steering give extra rewards (or penalty) on things that we want to emphasis more
def steering(curr_state, next_state):
    return 0


def total_reward(curr_state):
    return relative_successthroughput_reward(curr_state)
    # return sum(
    #     [
    #         #throughput_reward(curr_state, next_state),
    #         #success_reward(curr_state, next_state),
    #         relative_successthroughput_reward(curr_state, next_state),
    #         #steering(curr_state, next_state),
    #         #-penalty(curr_state, next_state),
    #     ]
    # )

def objective_achieved(curr_state):
    return curr_state[0] >= config.EXPECTED_SUCCESSTHROUGHPUT # 100% achieving target. ideal state
    # TODO enable below for training
    # or next_state[0] >= initial_state[0]*160/100 # 60% improvement from initial state. ideal for training
