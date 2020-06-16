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
		print(data)
		self.D[datestr] = data


class Data:
	W = ['월', '화', '수', '목', '금', '토', '일']
	D = dict()

	def __init__(self, datestr):
		self.datastr = datestr
		self.date = date.fromisoformat(datestr)
		print(self.W[self.date.weekday()])
		
	def add(self, item, count):
		self.D[item] = count

	def print(self):
		print("Data (%s %s)"%(self.date, self.W[self.date.weekday()]))

				
for xlsf in glob.glob("2020-06/*"):
	csvf = xlsf.replace(".xls", ".csv")
	if (os.path.exists(csvf)):
		print(csvf)
	else:
		xls = pd.read_excel(xlsf)
		xls.to_csv(csvf)
		print("%s converted to %s"%(xlsf, csvf))

datastore = DataStore()
data = None

# build dates
for csvf in glob.glob("2020-06/*.csv"):
	with open(csvf, 'r') as csvfile:
		csvrd = csv.reader(csvfile, delimiter=',')
		datestr = csvf.replace("/06", "").replace(".csv", "")
		data = Data(datestr)
		rowcnt = 0
		for row in csvrd:
			rowcnt = rowcnt + 1
			if (rowcnt < 4): continue
			if (row[2] == "합  계"): continue
			
			print("[" + row[2] + "]", row[4])
			data.add(row[2], int(row[4].replace(',', '')))

for data in datastore.D:
	print(data)
