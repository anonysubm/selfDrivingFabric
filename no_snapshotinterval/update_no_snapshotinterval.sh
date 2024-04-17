#!/usr/bin/env bash

# !TODO! Update hardcoded values
cp /home/ubuntu/selfConfiguringFabric/no_snapshotinterval/agent.py /home/ubuntu/selfConfiguringFabric/rl_model/
cp /home/ubuntu/selfConfiguringFabric/no_snapshotinterval/config.py /home/ubuntu/selfConfiguringFabric/
cp /home/ubuntu/selfConfiguringFabric/no_snapshotinterval/evaluation_function.py /home/ubuntu/selfConfiguringFabric/utils/
cp /home/ubuntu/selfConfiguringFabric/no_snapshotinterval/fabric_custom_env.py /home/ubuntu/selfConfiguringFabric/rl_model/
cp /home/ubuntu/selfConfiguringFabric/no_snapshotinterval/fabric_gym_env.py /home/ubuntu/selfConfiguringFabric/rl_model/
cp /home/ubuntu/selfConfiguringFabric/no_snapshotinterval/k8s-updateconfig.sh /home/ubuntu/selfConfiguringFabric/scripts/