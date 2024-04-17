#!/bin/bash

# !TODO! Update hardcoded values

#cd /home/ubuntu/hll3_opennebula
echo "k8s-update-caliper-config.sh"
echo $1
#yq e -i '.test.rounds[1].rateControl.opts.tps = $1' /home/ubuntu/hll3_opennebula/caliper/benchmarks/simplesupplychain/config.yaml
#cd /home/ubuntu/selfConfiguringFabric

sed -i "s/.*tps.*/            tps: $1/" /home/ubuntu/hll3_opennebula/caliper/benchmarks/simplesupplychain/config.yaml
#sed -i "0,/.*tps.*/s/.*tps.*/            tps: 1/" /home/ubuntu/hll3_opennebula/caliper/benchmarks/simplesupplychain/config.yaml