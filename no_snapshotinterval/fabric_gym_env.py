import gym
from gym.spaces.discrete import Discrete
from gym.spaces.multi_discrete import MultiDiscrete
from rl_model.agent import Agent
from rl_model.fabric_custom_env import Fabric
#from utils.logger import configure_logger, get_logger
import config
import time
import wandb
from config import (
    MAXIMUM_STEPS_PER_EPISODE, OBJECTIVE_REWARD_MULTIPLIER,
    discrete_action_space, #get_tps_value,
    #set_dqn_expected_throughput,
)
from copy import copy
from utils.evaluation_function import objective_achieved, total_reward
from gym import spaces
import numpy as np


class FabricEnv(gym.Env):
    @property
    def agent_pos(self):
        return self.agent.position

    def __init__(self, send_result=False, fixed_throughput=None, agent_random_start=True) -> None:
        print(f"fabric_gym_env.py: __init__()")
        super(FabricEnv, self).__init__()

        #self.logger = get_logger()
        
        self.env = Fabric()
        self.agent = Agent(random_start=agent_random_start)
        
        self.send_result = send_result
        self.fixed_throughput = fixed_throughput
        #self.current_state = (0, 0, 0, 0, 0, 0, 0)
        # we need to use the single discrete actions
        self.action_space = Discrete(len(discrete_action_space))
        #self.action_space = MultiDiscrete(len(discrete_action_space))
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(5,))

        # record and aggregrate results for informational purposes.
        self.send_result = send_result
        self.results = {
            "episode_rewards": [],
            "steps_per_episode": [],
            "expected_throughputs": [],
            "initial_states": [],
            "worst_states": [],
            "best_states": [],
            "best_configs": [],
        }

    # reset() called at the beginning of an episode, it returns an observation
    #def reset(self):
    def reset(self):
        print(f"fabric_gym_env.py: reset()")
        #set_dqn_expected_throughput(self.fixed_throughput)
        #self.env.set_tps(get_tps_value())
        #self.episode_step = 0
        try:
            self.episode_step = self.episode_step
        except:
            self.episode_step = 0

        self.env.rebuild_network(self.agent_pos, self.episode_step)
        #self.env.current_state = (0, 0, 0, 0, 0, 0, 0)
        self.initial_state = self.env.current_state
        
        # count the episodes
        try:
            self.episode_count += 1
        except:
            self.episode_count = 0

        self.results["episode_rewards"].append(0)
        self.results["steps_per_episode"].append(0)
        #self.results["expected_throughputs"].append(config.EXPECTED_THROUGHPUT)
        self.results["initial_states"].append(self.env.current_state)
        self.results["worst_states"].append(self.env.current_state)
        self.results["best_states"].append(self.env.current_state)
        self.results["best_configs"].append(
            {"max_message_count": self.agent_pos[0], "preferred_max_bytes": self.agent_pos[1], "batch_timeout": self.agent_pos[2]}
        )

        initial_obs = self.env.current_state
        return np.array(initial_obs).astype(np.float32)

    """
    step(action) called to take an action with the environment, it returns the next observation, the immediate reward, whether the episode is over and additional information
    """
    def step(self, action):
        print(f"fabric_gym_env.py: step()")
        print(f"self.episode_count: {self.episode_count}")
        print(f"self.episode_step: {self.episode_step}")
        
        self.episode_step += 1
        #if self.env.needs_rebuild():
            #self.logger.info(f"=== REBUILDING NETWORK BEFORE CONTINUING ===")
        #    print(f"=== REBUILDING NETWORK BEFORE CONTINUING ===")
        #    self.logger.info(
        #        f"=== state before rebuilding: {self.env.current_state} ==="
        #    )
            # rebuild_pinalty = self.env.current_state
        #self.env.rebuild_network(self.agent_pos)
            # rebuild_pinalty = total_reward(rebuild_pinalty, self.env.current_state) + 1
            #self.logger.info(
            #    f"=== state after rebuilding: {self.env.current_state} ==="
            #)
        #    print(f"=== state after rebuilding: {self.env.current_state} ===")

        # self.logger.info(
        #     f"for position {self.agent.position}, picked action {action} -> {discrete_action_space[action]}"
        # )
        print(f"for position {self.agent.position}, picked action {action} -> {discrete_action_space[action]}")
        
        

        # choosing block size
        self.agent.move(discrete_action_space[action])

        #self.logger.info(f"previous state = {self.env.current_state}")
        print(f"previous state = {self.env.current_state}")

        prev_state = copy(self.env.current_state)

        # update environment configuration & state
        self.env.update_env_config(self.agent_pos, self.episode_step)

        # calculate the reward
        reward = total_reward(self.env.current_state)

       

        #self.logger.info(f"reward obtained = {reward}")
        print(f"reward obtained = {reward}")

        # episode is done if max steps are exhausted or objective achieved
        done = objective_achieved(self.env.current_state)
        if done:
            #self.logger.info(f"=== Objective Achieved! ===")
            print(f"=== Objective Achieved! ===")
            reward = reward*OBJECTIVE_REWARD_MULTIPLIER

        self.results["episode_rewards"][self.episode_count] += reward
        self.results["steps_per_episode"][self.episode_count] += 1
        # update best state for positive reward (0 is also considered positive due to move penalty)
        # if (
        #     total_reward(
        #         self.results["best_states"][self.episode_count], self.env.current_state
        #     )
        #     >= 0
        # ):
        if (self.env.current_state[0] > self.results["best_states"][self.episode_count][0]):
            self.results["best_states"][self.episode_count] = self.env.current_state
            self.results["best_configs"][self.episode_count] = {
                "max_message_count": self.agent_pos[0], "preferred_max_bytes": self.agent_pos[1], "batch_timeout": self.agent_pos[2]
            }
        # if (
        #     total_reward(
        #         self.results["worst_states"][self.episode_count], self.env.current_state
        #     )
        #     < 0
        # ):
        if (self.env.current_state[0] < self.results["worst_states"][self.episode_count][0]):
            self.results["worst_states"][self.episode_count] = self.env.current_state


        #Reward is for previous step but variables are for the current step
        wandb.log({'max_message_count': self.agent_pos[0]}, step=self.episode_step)
        wandb.log({'preferred_max_bytes': self.agent_pos[1]}, step=self.episode_step)
        wandb.log({'batch_timeout': self.agent_pos[2]}, step=self.episode_step)
        #wandb.log({'snapshot_interval_size': self.agent_pos[3]}, step=self.episode_step)
        wandb.log({'discrete_action_space': discrete_action_space[action]}, step=self.episode_step)
        wandb.log({'reward': reward}, step=self.episode_step)
        wandb.log({'episode_number': self.episode_count}, step=self.episode_step)
        # no info passed for next step. should we pass results instead?
        info = {}
        return np.array(self.env.current_state).astype(np.float32), reward, done, info

    def close(self):
        print(f"fabric_gym_env.py: close()")
        pass
    
    def get_results(self):
        print(f"fabric_gym_env.py: get_results()")
        return self.results