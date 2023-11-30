#!/bin/bash
# script that sends requests to a url
curl -s "$1" | wc -c
