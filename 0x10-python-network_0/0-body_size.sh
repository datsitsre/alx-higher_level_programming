#!/bin/bash
# Post a URL and resquest
curl -s "$1" | wc -c
