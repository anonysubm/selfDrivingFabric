#!/usr/bin/env bash

# !TODO! Update hardcoded values
sed -i "s/.*value:.*/    value: $2/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
sed -i "s/.*pval:.*/    pval: $3/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
sed -i "s/.*tval:.*/    tval: $4s/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
sed -i "s/.*sval:.*/    sval: $5/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
#sed -i "s/.*tps.*/            tps: $6/" /home/ubuntu/hll3_opennebula/caliper/benchmarks/generator/config.yaml

cd /home/ubuntu/hll3_opennebula
## Uncomment for LEARNING_STARTS = 100
# if [[ $1 -lt 99 ]] && [[ $(($1 % 33)) == 0 ]]; then
#   echo "Updating transaction rate and restarting caliper"
#   >/home/ubuntu/hll3_opennebula/tpsupdate.txt
#   pkill -9 -f ./scripts/caliper_run.sh
#   pkill -9 -f caliper-manager
#   pkill -9 -f caliper-logs.txt
#   sleep 60s
#   while [ -f /home/ubuntu/hll3_opennebula/check_caliper.txt ]
#   do
#     echo "waiting for caliper restart..."
#     sleep 300s
#     echo "Delete check file"
#     rm /home/ubuntu/hll3_opennebula/check_caliper.txt
#   done
#elif [[ $(($1 % 100)) == 0 ]]; then
if [[ $(($1 % 100)) == 0 ]]; then
  echo "Updating transaction rate and restarting caliper"
  >/home/ubuntu/hll3_opennebula/tpsupdate.txt
  pkill -9 -f ./scripts/caliper_run.sh
  pkill -9 -f caliper-manager
  pkill -9 -f caliper-logs.txt
  sleep 60s
  while [ -f /home/ubuntu/hll3_opennebula/check_caliper.txt ]
  do
    echo "waiting for caliper restart..."
    sleep 300s
    echo "Delete check file"
    rm /home/ubuntu/hll3_opennebula/check_caliper.txt
  done
fi

#Comment line 43 for baseline runs
./scripts/network_update.sh

# argo logs @latest | grep "max_message_count:" | tail -1 >> /home/ubuntu/hll3_opennebula/configvars.txt
# argo logs @latest | grep "preferred_max_bytes:" | tail -1 >> /home/ubuntu/hll3_opennebula/configvars.txt
# argo logs @latest | grep "BatchTimeout:" | tail -1 >> /home/ubuntu/hll3_opennebula/configvars.txt
# argo logs @latest | grep "snapshot_interval_size:" | tail -1 >> /home/ubuntu/hll3_opennebula/configvars.txt
# echo "" >> /home/ubuntu/hll3_opennebula/configvars.txt

#sleep 10s
#>/home/ubuntu/hll3_opennebula/check.txt

while [ -f /home/ubuntu/hll3_opennebula/check.txt ]
do
  echo "waiting for fabric & caliper restart..."
  sleep 300s
  echo "Delete check file"
  rm /home/ubuntu/hll3_opennebula/check.txt
done
echo "waiting for network update to take effect..."
sleep 300s

cd /home/ubuntu/selfConfiguringFabric
