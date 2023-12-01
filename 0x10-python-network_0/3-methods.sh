#!/bin/bash
# script to print the allowed methods by a server
curl -s -X OPTIONS "$1" | grep Allow | cut -c 8-
