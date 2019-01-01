#!/bin/bash

WORKDIR="/etc/openvpn/manager"
LOGFILE="/var/log/openvpn/manager.log"


cd ${WORKDIR}

PID=$(ps axu | grep python3 | grep manager.py | grep -v grep | awk '{print $2}')

if [[ ! -n "${PID}" ]];
then
    nohup ./manager.py > ${LOGFILE} 2>&1 &
    echo "OpenVPN manager has started."
else
    echo "OpenVPN manager already running."
fi



