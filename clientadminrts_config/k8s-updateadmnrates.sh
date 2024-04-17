#!/usr/bin/env bash

# !TODO! Update hardcoded values
#[100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
#[60, 60, 60, 60, 60, 60, 60, 60, 60, 60]

a="("
b=","
c=")"
d=","
e="["
f="]"

if [[ $(($1 % 50)) == 0 ]]; then
  echo "Updating real transaction rate of caliper clients"
  tps=(100 50 10 300 100 100 300 50 100 10)
  tps=($(shuf -e "${tps[@]}"))
  printf -v tpsstr '%s, ' "${tps[@]}"
  tpsstr=${tpsstr/%" "/}
  tpsstr=${tpsstr/%$d/}
  tpsstr="[${tpsstr}]"
  echo $tpsstr

  sed -i "s/.*vvar wactualrate = .*/          var wactualrate = $tpsstr/" /home/ubuntu/hll3_opennebula/caliper/benchmarks/generator/getValues.js

fi



# $2 = 0.5 implies no change, 0 implies 10% decrease, 1 implies 10% increase
#learneddecision="(0, 0, 1, 0.5, 0, 1, 0.5, 0, 0, 0)"
learneddecision=$2
learneddecision=${learneddecision/$a/}
learneddecision=${learneddecision/$c/}
learneddecision=${learneddecision//$b/}
decisionarr=($learneddecision)
echo ${decisionarr[@]}

#learnedrate="[60, 60, 60, 60, 60, 100, 60, 60, 60, 60]"
learnedrate=$(cat /home/ubuntu/hll3_opennebula/caliper/benchmarks/generator/getValues.js | grep 'wlearnedrate' |  awk '{ for (i=4; i<=13;i++){ {printf $i} {printf " "} } }' )
learnedrate=${learnedrate/$e/}
learnedrate=${learnedrate/$f/}
learnedrate=${learnedrate//$b/}
ratearr=($learnedrate)
echo ${ratearr[@]}

#actualrate="[60, 60, 60, 60, 60, 100, 60, 60, 60, 60]"
actualrate=$(cat /home/ubuntu/hll3_opennebula/caliper/benchmarks/generator/getValues.js | grep 'wactualrate' |  awk '{ for (i=4; i<=13;i++){ {printf $i} {printf " "} } }')
actualrate=${actualrate/$e/}
actualrate=${actualrate/$f/}
actualrate=${actualrate//$b/}
actualratearr=($actualrate)
echo ${actualratearr[@]}

arrlength=${#ratearr[@]}
#multiplier=$(( 10/100 ))
 
for (( i=0; i<arrlength; i++ ));
do
  printf "Index %d RateValue %s DecisionValue %s\n" $i "${ratearr[$i]}" "${decisionarr[$i]}"
  if [ ${decisionarr[$i]} == 0 ]; then
    ratearr[$i]=$(( ${ratearr[$i]} - ${ratearr[$i]} / 10 ))
  elif [ ${decisionarr[$i]} == 1 ]; then
    temp=$(( ${ratearr[$i]} + ${ratearr[$i]} / 10 ))
    if [ $temp -lt ${actualratearr[$i]} ]; then
      ratearr[$i]=$temp
    else
      printf "No change"
    fi
  else
    printf "No change"
  fi
done

echo ${ratearr[@]}

printf -v ratestr '%s, ' "${ratearr[@]}"
ratestr=${ratestr/%" "/}
ratestr=${ratestr/%$d/}
ratestr="[${ratestr}]"
echo $ratestr

sed -i "s/.*var wlearnedrate = .*/          var wlearnedrate = $ratestr/" /home/ubuntu/hll3_opennebula/caliper/benchmarks/generator/getValues.js

cd /home/ubuntu/hll3_opennebula

echo "Updating admission rates and restarting caliper"
>/home/ubuntu/hll3_opennebula/rlupdate.txt
pkill -9 -f ./scripts/caliper_run.sh
pkill -9 -f caliper-manager
pkill -9 -f caliper-logs.txt
sleep 60s

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
