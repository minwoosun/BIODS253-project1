#!/bin/bash
# This run-script was generated with the help of ChatGPT.

if [ "$1" == "no_earthquake" ] || [ -z "$1" ]; then
  python pre_quake.py
elif [ "$1" == "earthquake" ]; then
  python post_quake.py
else
  echo "Error: invalid argument provided."
  echo "If you are going to add a command-line argument, please enter either 'no earthquake' or 'earthquake'."
  echo "If no command-line arguments are included, the script will run as if 'no earthquake' was entered."
fi