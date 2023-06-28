#!/bin/bash
# Takes a URL and display HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
