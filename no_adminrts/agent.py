"""
agent should choose from the available action, send it to environment to receive updated state and benchmarking result then calculate evaluation function result
"""
import random
from config import max_message_count, preferred_max_bytes, batch_timeout, snapshot_interval_size
from enum import Enum


class PossibleAction(Enum):
    INCREASE_BLOCK_SIZE = 0
    DECREASE_BLOCK_SIZE = 1
    INCREASE_PREFERRED_MAX_BYTES = 2
    DECREASE_PREFERRED_MAX_BYTES = 3
    INCREASE_BATCH_TIMEOUT = 4
    DECREASE_BATCH_TIMEOUT = 5
    INCREASE_SNAPSHOT_INTERVAL_SIZE = 6
    DECREASE_SNAPSHOT_INTERVAL_SIZE = 7


class Agent:
    def __init__(self, random_start=True):
        if random_start:
            self.block_size_choice = random.choice(max_message_count)
            self.preferred_max_bytes_choice = random.choice(preferred_max_bytes)
            self.batch_timeout_choice = random.choice(batch_timeout)
            self.snapshot_interval_size_choice = random.choice(snapshot_interval_size)
        else:
            self.block_size_choice = 10
            self.preferred_max_bytes_choice = 2
            self.batch_timeout_choice = 2
            self.snapshot_interval_size_choice = 16

    @property
    def position(self):
        return (self.block_size_choice, self.preferred_max_bytes_choice, self.batch_timeout_choice, self.snapshot_interval_size_choice)

    # get available actions based on state
    def available_actions(self):
        max_size = self.block_size_choice == max_message_count[-1]
        min_size = self.block_size_choice == max_message_count[0]
        max_preferred_max_bytes = self.preferred_max_bytes_choice == preferred_max_bytes[-1]
        min_preferred_max_bytes = self.preferred_max_bytes_choice == preferred_max_bytes[0]
        max_batch_timeout = self.batch_timeout_choice == batch_timeout[-1]
        min_batch_timeout = self.batch_timeout_choice == batch_timeout[0]
        max_snapshot_interval_size = self.snapshot_interval_size_choice == snapshot_interval_size[-1]
        min_snapshot_interval_size = self.snapshot_interval_size_choice == snapshot_interval_size[0]

        possible_actions = list(PossibleAction)
        
        if max_size:
            self._remove_action(possible_actions, PossibleAction.INCREASE_BLOCK_SIZE)
        if min_size:
            self._remove_action(possible_actions, PossibleAction.DECREASE_BLOCK_SIZE)
        if min_preferred_max_bytes:
            self._remove_action(possible_actions, PossibleAction.DECREASE_PREFERRED_MAX_BYTES)
        if max_preferred_max_bytes:
            self._remove_action(possible_actions, PossibleAction.INCREASE_PREFERRED_MAX_BYTES)  
        if min_batch_timeout:    
            self._remove_action(possible_actions, PossibleAction.DECREASE_BATCH_TIMEOUT)
        if max_batch_timeout:
            self._remove_action(possible_actions, PossibleAction.INCREASE_BATCH_TIMEOUT)
        if min_snapshot_interval_size:
            self._remove_action(possible_actions, PossibleAction.DECREASE_SNAPSHOT_INTERVAL_SIZE)
        if max_snapshot_interval_size:
            self._remove_action(possible_actions, PossibleAction.INCREASE_SNAPSHOT_INTERVAL_SIZE)

        return tuple(possible_actions)

    def _remove_action(self, arr, act):
        try:
            arr.remove(act)
        except ValueError:
            pass
    
    # directly move from one action to another
    def move(self, agent_pos):
        self.block_size_choice = agent_pos[0]
        self.preferred_max_bytes_choice = agent_pos[1]
        self.batch_timeout_choice = agent_pos[2]
        self.snapshot_interval_size_choice = agent_pos[3]
        
    # one step from one possible action to neighbour action
    def step(self, choice):
        size_idx = max_message_count.index(self.block_size_choice)
        preferred_max_bytes_idx = preferred_max_bytes.index(self.preferred_max_bytes_choice)
        batch_timeout_idx = batch_timeout.index(self.batch_timeout_choice)
        snapshot_interval_size_idx = snapshot_interval_size.index(self.snapshot_interval_size_choice)

        if choice == PossibleAction.INCREASE_BLOCK_SIZE:
            self.block_size_choice = max_message_count[size_idx + 1]
        elif choice == PossibleAction.DECREASE_BLOCK_SIZE:
            self.block_size_choice = max_message_count[size_idx - 1]
        elif choice == PossibleAction.INCREASE_PREFERRED_MAX_BYTES:
            self.preferred_max_bytes_choice = preferred_max_bytes[preferred_max_bytes_idx + 1]
        elif choice == PossibleAction.DECREASE_PREFERRED_MAX_BYTES:
            self.preferred_max_bytes_choice = preferred_max_bytes[preferred_max_bytes_idx - 1]
        elif choice == PossibleAction.INCREASE_BATCH_TIMEOUT:
            self.batch_timeout_choice = batch_timeout[batch_timeout_idx + 1]
        elif choice == PossibleAction.DECREASE_BATCH_TIMEOUT:
            self.batch_timeout_choice = batch_timeout[batch_timeout_idx - 1]
        elif choice == PossibleAction.INCREASE_SNAPSHOT_INTERVAL_SIZE:
            self.snapshot_interval_size_choice = snapshot_interval_size[snapshot_interval_size_idx + 1]
        elif choice == PossibleAction.DECREASE_SNAPSHOT_INTERVAL_SIZE:
            self.snapshot_interval_size_choice = snapshot_interval_size[snapshot_interval_size_idx - 1]
        else:
            raise ValueError("Invalid action")
