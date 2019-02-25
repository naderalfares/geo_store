#!/bin/bash

var="./out/"
var="$var$2"
mkdir $var
var="$var/$2"
echo $var

python3 placement.py -f $1 -o "$var-opt.json" -H min_cost
python3 placement.py -f $1 -o "$var-abd.json" -H min_cost -b -t abd
python3 placement.py -f $1 -o "$var-cas.json" -H min_cost -b -t cas
python3 placement.py -f $1 -o "$var-rep.json" -H min_cost -b -t cas -k 1
python3 placement.py -f $1 -o "$var-opt-l.json" -H min_latency
python3 placement.py -f $1 -o "$var-abd-l.json" -H min_latency -b -t abd
python3 placement.py -f $1 -o "$var-cas-l.json" -H min_latency -b -t cas
python3 placement.py -f $1 -o "$var-rep-l.json" -H min_latency -b -t cas -k 1
python3 placement.py -f $1 -o "$var-opt-v.json" -H min_cost -v
python3 placement.py -f $1 -o "$var-abd-v.json" -H min_cost -b -t abd -v
python3 placement.py -f $1 -o "$var-cas-v.json" -H min_cost -b -t cas -v
python3 placement.py -f $1 -o "$var-rep-v.json" -H min_cost -b -t cas -k 1 -v
python3 placement.py -f $1 -o "$var-opt-lv.json" -H min_latency -v
python3 placement.py -f $1 -o "$var-abd-lv.json" -H min_latency -b -t abd -v
python3 placement.py -f $1 -o "$var-cas-lv.json" -H min_latency -b -t cas -v
python3 placement.py -f $1 -o "$var-rep-lv.json" -H min_latency -b -t cas -k 1 -v
