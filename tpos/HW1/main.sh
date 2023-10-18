#!/bin/bash
command=$1
value=$2
source ./venv/bin/activate
if [ "$command" = "start" ]; then
    ./venv/bin/python main.py start $value
elif [ "$command" = "stop" ]; then
    ./venv/bin/python main.py stop $value
elif [ "$command" = "stop_all" ]; then
    ./venv/bin/python main.py stop_all
else
    echo """Wrong command. Use it as:
    start <number of sessions to create, int>
    stop <number of session to kill, int>
    stop_all"""
fi
