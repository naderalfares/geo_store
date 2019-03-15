#!/bin/bash

var="./tests/traces/trace_"
var="$var$2"
mkdir $var

python3 trace_gen.py -f $1 -i $2 
