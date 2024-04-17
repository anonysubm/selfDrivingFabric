"""
environment is an abstraction to connect with existing Hyperledger Fabric instance
contains state and run the benchmarking function for every agent's action

observation space?
"""

from subprocess import TimeoutExpired
from utils.caliper_report_parser import parse_caliper_log
#from utils.database import MongoConnector
#from utils.logger import get_logger
from config import (
    #REBUILD_LIMIT,
    #TX_DURATION,
    max_message_count, preferred_max_bytes, batch_timeout, snapshot_interval_size
)
import math
import numpy as np
from matplotlib import style
import subprocess

style.use("ggplot")


class Fabric:
    """
    state is defined as union between current tps and success/failure difference
    """

    def __init__(self):
        print(f"fabric_custom_env.py: init()")
        #self.logger = get_logger()
        self.current_state = (0, 0, 0, 0, 0, 0)
        self.q_table = {}
        #self.db = MongoConnector()
        self.target_tps = 0
        self.tx_submitted = 0
        #rc = subprocess.call("./scripts/copy_config_init.sh")
        #rc = subprocess.call("./scripts/k8s-rebuild-network.sh")
        #rc = subprocess.call("./scripts/k8s-execute-caliper.sh")
        #rc = subprocess.call("./scripts/copy_config_no_init.sh")
    
     

    # setting send rate
    #def set_tps(self, tps):
        #print(f"fabric_custom_env.py: set_tps()")
    #     self.target_tps = tps
    #     assets = math.ceil(tps * 2)
        #print(f"=== NEW CALIPER ROUND ===")
        #rc = subprocess.call("./scripts/kill_caliper_processes.sh")
        #rc = subprocess.call(["./scripts/k8s-update-caliper-config.sh", str(tps)])
        #subprocess.Popen(["./scripts/k8s-execute-caliper.sh"])
        #rc = subprocess.call(["sleep 20s"])
        #rc = subprocess.call("./scripts/k8s-execute-caliper.sh")
        #self.logger.info(f"=== UPDATE CALIPER CONFIG WITH VALUE {tps} {assets} ===")
        #update_process = subprocess.Popen(
        #    ["sudo", "./scripts/k8s-update-caliper-config.sh", str(tps), str(assets)],
        #    stdout=subprocess.PIPE,
        #    stderr=subprocess.DEVNULL,
        #)
        #_, err = update_process.communicate()
        #self.logger.debug(f"error while updating tps {err}")

    # rebuild fabric
    def rebuild_network(self, agent_conf, episode_step):
    #     print(f"fabric_custom_env.py: rebuild_network()")
    #     print(f"=== REBUILDING NETWORK ===")
    #     if block_size is 10:
    #         rc = subprocess.call("./scripts/k8s-rebuild-network.sh && ./scripts/k8s-execute-caliper.sh", shell=True)

    #     else:
    #         rc = subprocess.call("./scripts/k8s-rebuild-network.sh")
    #         rc = subprocess.call(["./scripts/k8s-updateconfig.sh", str(block_size)])
    #         rc = subprocess.call("./scripts/k8s-execute-caliper.sh")
    #     #self.logger.info(f"=== REBUILDING NETWORK ===")
    #     #if block_size is 10:
    #     #    command = f"./scripts/k8s-rebuild-network.sh && ./scripts/k8s-execute-caliper.sh "
    #     #else:
    #     #    command = f"./scripts/k8s-rebuild-network.sh && ./scripts/k8s-updateconfig.sh {block_size} && ./scripts/k8s-execute-caliper.sh "

    #     #rebuild_process = subprocess.Popen(
    #     #    [command],
    #     #    shell=True,
    #     #    stdout=subprocess.PIPE,
    #     #    stderr=subprocess.DEVNULL,
    #     #)
    #     #_, err = rebuild_process.communicate()
    #     #self.logger.debug(f"error while rebuilding network {err}")

        self.update_current_state(agent_conf, episode_step)
    #     self.tx_submitted = 0

    # update fabric config
    def update_env_config(self, agent_conf, episode_step, fixed_config=True):
        print(f"fabric_custom_env.py: update_env_config()")
        print(f"LIST OF CONFIG VARIABLES: {str(agent_conf)}")
        rc = subprocess.call(["./scripts/k8s-updateconfig.sh", str(agent_conf[0]), str(agent_conf[1]), str(agent_conf[2]), str(agent_conf[3])])
        #rc = subprocess.call("./scripts/k8s-execute-caliper.sh")
        #rc = subprocess.call("./scripts/k8s-updateconfig.sh {block_size} && ./scripts/k8s-execute-caliper.sh ", shell=True)
        #command = f"./scripts/k8s-updateconfig.sh {block_size} && ./scripts/k8s-execute-caliper.sh "
        #update_process = subprocess.Popen(
        #    [command],
        #    shell=True,
        #    stdout=subprocess.PIPE,
        #    stderr=subprocess.DEVNULL,
        #)
        
        try:
            # combine update and benchmark
            #_, err = update_process.communicate()
            self.update_current_state(agent_conf, episode_step, fixed_config)
            #self.logger.debug(f"error during process {err}")
        except TimeoutExpired:
            update_process.kill()
            # benchmark_process.kill()
            #self.logger.info(f"benchmark timeout occured")
            print(f"benchmark timeout occured")
            self.current_state = (0, 0, 0, 0, 0, 0)  # signal an error

        return self.current_state

    # parse the caliper result
    def update_current_state(self, agent_conf, episode_step, fixed_config=True):
        print(f"fabric_custom_env.py: update_current_state()")
        print(f"LIST OF CONFIG VARIABLES: {str(agent_conf)}")
        # TODO change the keyword for different transaction/chaincode. Provide multiple keywords for multiple benchmarks.
        raw_states = parse_caliper_log(episode_step) # Transaction keyword
        print(f"===== THE STATE IS {raw_states} =====")
        
        try:
            # transaction per second (succ/(last commit time - first submit time))
            #throughputs = np.array(
            #    [state["throughput"] for state in raw_states]
            #)
            # successes per second
            #successes = np.array(
            #    [state["success"] / TX_DURATION for state in raw_states]
            #)
            # average latency per transaction
            #latencies = np.array(
            #    [state["avg_latency"] for state in raw_states]
            #)
            #np.nan_to_num(throughputs, copy=False)
            #np.nan_to_num(successes, copy=False)
            #np.nan_to_num(latencies, copy=False)

            relative_successthroughputs = np.array(
                [state["relative_successthroughput"] for state in raw_states]
            )
            send_rates = np.array(
                [state["send_rate"] for state in raw_states]
            )
            np.nan_to_num(relative_successthroughputs, copy=False)
            np.nan_to_num(send_rates, copy=False)

            if fixed_config:
                size_idx = max_message_count.index(agent_conf[0])
                preferred_max_bytes_idx = preferred_max_bytes.index(agent_conf[1])
                batch_timeout_idx = batch_timeout.index(agent_conf[2])
                snapshot_interval_size_idx = snapshot_interval_size.index(agent_conf[3])
            else:
                size_idx = agent_conf[0]
                preferred_max_bytes_idx = agent_conf[1]
                batch_timeout_idx = agent_conf[2]
                snapshot_interval_size_idx = agent_conf[3]


            self.current_state = (
                round(np.average(relative_successthroughputs), 2),
                #math.ceil(np.average(throughputs)),
                #math.ceil(np.average(successes)),
                size_idx,
                preferred_max_bytes_idx,
                batch_timeout_idx,
                snapshot_interval_size_idx,
                round(np.average(send_rates), 2)
            )
            # stupid approximation of tx limit.
            #self.tx_submitted += math.ceil(np.sum(successes) * TX_DURATION)
            # save to mongodb database
            #self.save_state_to_db(block_size, raw_states)
        except Exception as e:
            #self.logger.info(f"report parsing error {e}")
            print(f"report parsing error {e}")
            self.current_state = (0, 0, 0, 0, 0, 0)  # signal an error

        #self.logger.info(
        #    f"update state finished for size {block_size} with results {self.current_state}"
        #)
        print(f"update state finished for size {agent_conf} with results {self.current_state}")

    #def needs_rebuild(self):
    #    print(f"fabric_custom_env.py: needs_rebuild()")
    #    return (
    #        self.tx_submitted >= REBUILD_LIMIT or self.current_state[0] == 0
    #    )  # if throughput is 0, something is wrong

    #def save_state_to_db(self, size, raw):
    #    config = {
    #        "target_tps": self.target_tps,
    #        "batch_size": size,
    #    }
    #    self.db.insertData(config, raw)
