#!/bin/bash
command=$1
value=$2
if [ "$command" = "start" ]; then
    bash python3 main.py start $value
elif [ "$command" = "stop" ]; then
    bash python3 main.py stop $value
elif [ "$command" = "stop_all" ]; then
    bash python3 main.py stop_all
else
    echo """Wrong command. Use it as:
    start <number of sessions to create, int>
    stop <number of session to kill, int>
    stop_all"""
fi
