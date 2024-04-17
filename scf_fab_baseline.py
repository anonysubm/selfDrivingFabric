import gym
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

def run_scf():
    log_dir = "/home/ubuntu/nilm/temp/chacko/scf_exps_real_large/"
    os.makedirs(log_dir, exist_ok=True)
    
    # Initialize wandb
    wandb_config = {"env_name": "scf_fab_baseline"}
    
    run = wandb.init(project="scf_fab_baseline", config=wandb_config, monitor_gym=True, save_code=True, dir=log_dir)
    
    run.finish()

try:
    run_scf()
except Exception as e:
    wandb.alert(title="Error", text=e)

    
