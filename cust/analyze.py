#!/opt/anaconda3/bin/python3

import pandas as pd
import glob, os
import csv
import datetime
from datetime import date

class DataStore:
	D = dict()
	def __init__(self):
			None

	def add(self, datestr, data):
			self.D[datestr] = data

class Data:
	W = ['월', '화', '수', '목', '금', '토', '일']
	D = dict()

	def __init__(self, datestr):
		self.datastr = datestr
		self.date = date.fromisoformat(datestr)
		
	def add(self, item, count):
		self.D[item] = count

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

datastore = DataStore()
data = None
for csvf in glob.glob("data/*.csv"):
	with open(csvf, 'r') as csvfile:
		csvrd = csv.reader(csvfile, delimiter=',')
		for row in csvrd:
			if (row[0] == '0'):
				datestr = row[2].split(" ")[2]
				data = Data(datestr)
				datastore.add(datestr, data)
			elif (row[0].isnumeric() and int(row[0]) > 1):
				print(row[2], row[4])
				data.add(row[2], int(row[4].replace(',', '')))
