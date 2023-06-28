#!/bin/bash
# URL send a POST request to the passwd URL and displays
curl -s -X POST "${1}" -d '{"email":"test@gmail.com", "subject":"I will always be here for PLD"}'
