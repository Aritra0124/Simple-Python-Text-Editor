#!/bin/sh

MODULE1="python3"
MODULE2="python3-tk"

echo "checking required modules are installed or not"

#------------------python3--------------------#

if dpkg -l | grep "$MODULE1" >> /dev/null ; then
  echo "$MODULE1 is loaded!"
else
  echo "$MODULE1 is not loaded!"
fi

#------------------python3-tk------------------#

if dpkg -l | grep "$MODULE2" >> /dev/null ; then
  echo "$MODULE2 is loaded!"
else
  echo "$MODULE2 is not loaded!"
fi
