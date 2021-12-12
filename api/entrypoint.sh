#!/bin/bash
cd /home/stop-fraud \
&& export PYTHONDONTWRITEBYTECODE=1 \
&& uvicorn main:app --host=0.0.0.0 --port=80 --reload
