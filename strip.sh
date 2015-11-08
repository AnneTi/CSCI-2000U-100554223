#!/bin/bash
# Anne Tissera 100554223

echo "Enter a value for k: "
read k 

echo "Enter a value for m: "
read m

echo "Enter the filename: "
read filename 

head -n -$m $filename | tail -n +$k > gadsby_stripped.txt




