#!/bin/bash

find $1 \( -name "*_maxbin" -o -name "*_metabat" -o -name "*_concoct" -o -name "*_das" \) -type d -exec ./submit.sh {} $2 \;