#!/bin/bash

echo "Content-Type: text/plain"
echo
echo "*** ENVIRONMENT VARIABLES***"
strings /proc/$$/environ
