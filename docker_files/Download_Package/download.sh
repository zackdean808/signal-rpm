#!/bin/bash

cd /tmp
apt-get download signal-desktop 2&>1 
if [ $? -ne 0 ]
then 
	echo "Dowload success"
fi 
