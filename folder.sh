#!/bin/bash

find $1 -iname "*_maxbin" -type d -exec ./submit.sh {} $2 \;