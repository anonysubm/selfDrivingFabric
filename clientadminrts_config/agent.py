"""
agent should choose from the available action, send it to environment to receive updated state and benchmarking result then calculate evaluation function result
"""
import random
from config import client_1, client_2, client_3, client_4, client_5, client_6, client_7, client_8, client_9, client_10
from enum import Enum


class PossibleAction(Enum):
    INCREASE_CLIENT_1 = 0
    DECREASE_CLIENT_1 = 1
    INCREASE_CLIENT_2 = 2
    DECREASE_CLIENT_2 = 3
    INCREASE_CLIENT_3 = 4
    DECREASE_CLIENT_3 = 5
    INCREASE_CLIENT_4 = 6
    DECREASE_CLIENT_4 = 7
    INCREASE_CLIENT_5 = 8
    DECREASE_CLIENT_5 = 9
    INCREASE_CLIENT_6 = 10
    DECREASE_CLIENT_6 = 11
    INCREASE_CLIENT_7 = 12
    DECREASE_CLIENT_7 = 13
    INCREASE_CLIENT_8 = 14
    DECREASE_CLIENT_8 = 15
    INCREASE_CLIENT_9 = 16
    DECREASE_CLIENT_9 = 17
    INCREASE_CLIENT_10 = 18
    DECREASE_CLIENT_10 = 19


class Agent:
    def __init__(self, random_start=True):
        if random_start:
            self.client_1_choice = random.choice(client_1)
            self.client_2_choice = random.choice(client_2)
            self.client_3_choice = random.choice(client_3)
            self.client_4_choice = random.choice(client_4)
            self.client_5_choice = random.choice(client_5)
            self.client_6_choice = random.choice(client_6)
            self.client_7_choice = random.choice(client_7)
            self.client_8_choice = random.choice(client_8)
            self.client_9_choice = random.choice(client_9)
            self.client_10_choice = random.choice(client_10)
        else:
            self.client_1_choice = random.choice(client_1)
            self.client_2_choice = random.choice(client_2)
            self.client_3_choice = random.choice(client_3)
            self.client_4_choice = random.choice(client_4)
            self.client_5_choice = random.choice(client_5)
            self.client_6_choice = random.choice(client_6)
            self.client_7_choice = random.choice(client_7)
            self.client_8_choice = random.choice(client_8)
            self.client_9_choice = random.choice(client_9)
            self.client_10_choice = random.choice(client_10)

    @property
    def position(self):
        return (self.client_1_choice, self.client_2_choice, self.client_3_choice, self.client_4_choice, self.client_5_choice, self.client_6_choice, self.client_7_choice, self.client_8_choice, self.client_9_choice, self.client_10_choice)

    # get available actions based on state
    def available_actions(self):
        max_client_1 = self.client_1_choice == client_1[-1]
        min_client_1 = self.client_1_choice == client_1[0]
        max_client_2 = self.client_2_choice == client_2[-1]
        min_client_2 = self.client_2_choice == client_2[0]
        max_client_3 = self.client_3_choice == client_3[-1]
        min_client_3 = self.client_3_choice == client_3[0]
        max_client_4 = self.client_4_choice == client_4[-1]
        min_client_4 = self.client_4_choice == client_4[0]
        max_client_5 = self.client_5_choice == client_5[-1]
        min_client_5 = self.client_5_choice == client_5[0]
        max_client_6 = self.client_6_choice == client_6[-1]
        min_client_6 = self.client_6_choice == client_6[0]
        max_client_7 = self.client_7_choice == client_7[-1]
        min_client_7 = self.client_7_choice == client_7[0]
        max_client_8 = self.client_8_choice == client_8[-1]
        min_client_8 = self.client_8_choice == client_8[0]
        max_client_9 = self.client_9_choice == client_9[-1]
        min_client_9 = self.client_9_choice == client_9[0]
        max_client_10 = self.client_10_choice == client_10[-1]
        min_client_10 = self.client_10_choice == client_10[0]

        possible_actions = list(PossibleAction)
        
        if max_client_1:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_1)
        if min_client_1:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_1)
        if max_client_2:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_2)
        if min_client_2:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_2)
        if max_client_3:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_3)
        if min_client_3:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_3)
        if max_client_4:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_4)
        if min_client_4:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_4)
        if max_client_5:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_5)
        if min_client_5:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_5)
        if max_client_6:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_6)
        if min_client_6:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_6)
        if max_client_7:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_7)
        if min_client_7:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_7)
        if max_client_8:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_8)
        if min_client_8:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_8)
        if max_client_9:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_9)
        if min_client_9:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_9)
        if max_client_10:
            self._remove_action(possible_actions, PossibleAction.INCREASE_CLIENT_10)
        if min_client_10:
            self._remove_action(possible_actions, PossibleAction.DECREASE_CLIENT_10)

        return tuple(possible_actions)

    def _remove_action(self, arr, act):
        try:
            arr.remove(act)
        except ValueError:
            pass
    
    # directly move from one action to another
    def move(self, agent_pos):
        self.client_1_choice = agent_pos[0]
        self.client_2_choice = agent_pos[1]
        self.client_3_choice = agent_pos[2]
        self.client_4_choice = agent_pos[3]
        self.client_5_choice = agent_pos[4]
        self.client_6_choice = agent_pos[5]
        self.client_7_choice = agent_pos[6]
        self.client_8_choice = agent_pos[7]
        self.client_9_choice = agent_pos[8]
        self.client_10_choice = agent_pos[9]
        
    # one step from one possible action to neighbour action
    def step(self, choice):
        client_1_idx = client_1.index(self.client_1_choice)
        client_2_idx = client_2.index(self.client_2_choice)
        client_3_idx = client_3.index(self.client_3_choice)
        client_4_idx = client_4.index(self.client_4_choice)
        client_5_idx = client_5.index(self.client_5_choice)
        client_6_idx = client_6.index(self.client_6_choice)
        client_7_idx = client_7.index(self.client_7_choice)
        client_8_idx = client_8.index(self.client_8_choice)
        client_9_idx = client_9.index(self.client_9_choice)
        client_10_idx = client_10.index(self.client_10_choice)

        if choice == PossibleAction.INCREASE_CLIENT_1:
            self.client_1_choice = client_1[client_1_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_1:
            self.client_1_choice = client_1[client_1_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_2:
            self.client_2_choice = client_2[client_2_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_2:
            self.client_2_choice = client_2[client_2_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_3:
            self.client_3_choice = client_3[client_3_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_3:
            self.client_3_choice = client_3[client_3_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_4:
            self.client_4_choice = client_4[client_4_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_4:
            self.client_4_choice = client_4[client_4_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_5:
            self.client_5_choice = client_5[client_5_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_5:
            self.client_5_choice = client_5[client_5_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_6:
            self.client_6_choice = client_6[client_6_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_6:
            self.client_6_choice = client_6[client_6_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_7:
            self.client_7_choice = client_7[client_7_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_7:
            self.client_7_choice = client_7[client_7_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_8:
            self.client_8_choice = client_8[client_8_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_8:
            self.client_8_choice = client_8[client_8_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_9:
            self.client_9_choice = client_9[client_9_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_9:
            self.client_9_choice = client_9[client_9_idx - 1]
        elif choice == PossibleAction.INCREASE_CLIENT_10:
            self.client_10_choice = client_10[client_10_idx + 1]
        elif choice == PossibleAction.DECREASE_CLIENT_10:
            self.client_10_choice = client_10[client_10_idx - 1]
        else:
            raise ValueError("Invalid action")
