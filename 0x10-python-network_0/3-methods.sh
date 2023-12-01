#!/bin/bash
# script to print the allowed methods by a server
curl -sI -X OPTIONS "$1" | grep Allow | cut -c 8-
