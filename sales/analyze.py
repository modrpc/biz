#!/opt/anaconda3/bin/python3

import pandas as pd
import glob, os

for csvf in glob.glob("*.csv"):
	csv_reader = csv.reader(csvf, delimiter=',')
    for row in csv_reader:

	
