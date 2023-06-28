#!/bin/bash
# URL send a POST request to the passwd URL and displays
curl -s -X POST -d '{"email":"test@gmail.com","subject":"I will always be here for PLD"}' "${1}"
