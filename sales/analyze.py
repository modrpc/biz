#!/opt/anaconda3/bin/python3

import pandas as pd
import glob, os
import csv
import datetime
from datetime import date

class Data:
	W = ['월', '화', '수', '목', '금', '토', '일']
	def __init__(self, datestr):
		self.date = date.fromisoformat(datestr)
		
	def print(self):
		print("Data (%s %s)"%(self.date, self.W[self.date.weekday()]))
				
for xlsf in glob.glob("data/*.xls"):
	csvf = xlsf.replace(".xls", ".csv")
	if (os.path.exists(csvf)):
		print(csvf)
	else:
		xls = pd.read_excel(xlsf)
		xls.to_csv(csvf)
		print("%s converted to %s"%(xlsf, csvf))
				
for csvf in glob.glob("data/*.csv"):
	with open(csvf, 'r') as csvfile:
		csvrd = csv.reader(csvfile, delimiter=',')
		for row in csvrd:
			if (row[0] == '0'):
				datestr = row[2].split(" ")[2]
				data = Data(datestr)
				data.print()
				break
		                                
