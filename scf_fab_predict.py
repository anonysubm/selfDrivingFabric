import gym
#from gym import spaces
#import numpy as np
from gym.wrappers import TimeLimit
import os
import wandb
from stable_baselines3 import DQN
from stable_baselines3.dqn import MlpPolicy
import config 
from wandb.integration.sb3 import WandbCallback
from rl_model.fabric_gym_env import FabricEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from config import discrete_action_space

def run_scf_predict():
    log_dir = "/home/ubuntu/nilm/temp/chacko/scf_exps_real_large/"
    os.makedirs(log_dir, exist_ok=True)
    model_dir = "/home/ubuntu/nilm/temp/chacko/scf_exps_real_large/models/"
    os.makedirs(model_dir, exist_ok=True)
    # Create log dir
    #log_dir = "tmp/"
    #os.makedirs(log_dir, exist_ok=True)

    env = FabricEnv(fixed_throughput=config.FIXED_THROUGHPUT, agent_random_start=False)
    env = TimeLimit(env, max_episode_steps=config.MAXIMUM_STEPS_PER_EPISODE)
    env = make_vec_env(lambda: env, n_envs=1)
    
    # Initialize wandb
    wandb_config = {
        "policy_type": "MlpPolicy",
        "total_timesteps": config.MAXIMUM_STEPS_PER_EPISODE * config.NUMBER_OF_EPISODES,
        "env_name": "scf_fab_real_large",
        "learning_rate": config.LEARNING_RATE}
    
    run = wandb.init(project="scf_fab_real_large", config=wandb_config, monitor_gym=True, save_code=True, dir=log_dir)
    # Instantiate the agent
    model = DQN(
        MlpPolicy,
        env,
        verbose=1,
        learning_rate=config.LEARNING_RATE,
        learning_starts=config.LEARNING_STARTS,
        exploration_fraction=config.EXPLORATION_FRACTION,
        #tensorboard_log=log_dir,
    )
    model_name = "/home/ubuntu/nilm/temp/chacko/scf_exps_real_large/models/ybrsknxy/model.zip"
    model.load(model_name)

    obs_temp = env.env_method("reset")[0]
    obs = obs_temp[0]
    initial_obs = obs

    print(f"=== prediction with starting obs {obs} ===")
    done = False
    info = {}
    selected_actions = [env.get_attr("agent")[0].position]
    while not done:
        actions, _ = model.predict(obs, deterministic=True)
        obs, reward, _done1, _done2, info = env.env_method("step", actions)[0]
        print(f"==== _done1: {_done1} _done2: {_done2}====")
        print(f"predicted action {discrete_action_space[actions]} resulting in {obs} and {reward} reward")
        if reward < 0 or _done1:
            done = True
            print(f"==== WHILE ENDED reward: {reward} _done1: {_done1} _done2: {_done2}====")
        else:
            selected_actions.append(discrete_action_space[actions])
    print(f"==== prediction ends {selected_actions}====")
    print(f"recap: {model_name}; {initial_obs}; {selected_actions}; {obs}")


    result = env.env_method("get_results")
    print(f"DQN PREDICT RUN COMPLETE")
    print(f"DQN RESULTS: {str(result)}")

    run.finish()

try:
    for _ in range(1000):
        run_scf_predict()
except Exception as e:
    wandb.alert(title="Error", text=e)

    
