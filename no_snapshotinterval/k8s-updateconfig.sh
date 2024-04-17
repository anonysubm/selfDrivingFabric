#!/usr/bin/env bash

# !TODO! Update hardcoded values
sed -i "s/.*value:.*/    value: $1/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
sed -i "s/.*pval:.*/    pval: $2/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
sed -i "s/.*tval:.*/    tval: $3s/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
#sed -i "s/.*sval:.*/    sval: $4/" /home/ubuntu/hll3_opennebula/fabric/channel-update/values.yaml
#sed -i "s/.*tps.*/            tps: $5/" /home/ubuntu/hll3_opennebula/caliper/benchmarks/generator/config.yaml

cd /home/ubuntu/hll3_opennebula

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
sleep 120s

cd /home/ubuntu/selfConfiguringFabric
