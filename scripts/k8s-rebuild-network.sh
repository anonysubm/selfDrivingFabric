#!/usr/bin/env bash

# !TODO! Update hardcoded values

cd /home/ubuntu/hll3_opennebula

./scripts/network_delete.sh

sleep 10s

./scripts/network_run.sh

cd /home/ubuntu/selfConfiguringFabric