#!/usr/bin/env bash

# !TODO! Update hardcoded values
cp /home/ubuntu/selfConfiguringFabric/no_adminrts/agent.py /home/ubuntu/selfConfiguringFabric/rl_model/
cp /home/ubuntu/selfConfiguringFabric/no_adminrts/config.py /home/ubuntu/selfConfiguringFabric/
cp /home/ubuntu/selfConfiguringFabric/no_adminrts/evaluation_function.py /home/ubuntu/selfConfiguringFabric/utils/
cp /home/ubuntu/selfConfiguringFabric/no_adminrts/fabric_custom_env.py /home/ubuntu/selfConfiguringFabric/rl_model/
cp /home/ubuntu/selfConfiguringFabric/no_adminrts/fabric_gym_env.py /home/ubuntu/selfConfiguringFabric/rl_model/
cp /home/ubuntu/selfConfiguringFabric/no_adminrts/k8s-updateconfig.sh /home/ubuntu/selfConfiguringFabric/scripts/