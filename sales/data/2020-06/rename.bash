#!/bin/bash

for file in *; do
	mv "$file" "$(basename "$file").xls"
done
