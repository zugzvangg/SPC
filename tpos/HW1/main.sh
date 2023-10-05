#!/bin/bash
command=$1
value=$2
if [ "$command" = "start" ]; then
    bash python3 main.py start $value
fi

