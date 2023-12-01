#!/bin/bash
# script to print the allowed methods by a server
curl -sI "$1" | grep Allow | cut -c 8-
