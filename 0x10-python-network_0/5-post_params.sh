#!/bin/bash
# script that sends a POST request to a server
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d {"email": "test@gmail.com", "subject": "I will always be here for PLD" "$1"
