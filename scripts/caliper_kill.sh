#!/usr/bin/env bash

pkill -9 -f ./scripts/caliper_run.sh
pkill -9 -f caliper-logs.txt
echo "Caliper Killed" >> /home/ubuntu/hll3_opennebula/caliper/failure_logs.txt
echo "waiting for caliper restart..."
sleep 180s