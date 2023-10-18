#!/bin/bash
chmod +x main.sh
chmod +x install.sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
