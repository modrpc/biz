#!//bin/python3

import pandas as pd
import glob, os
import csv
import datetime
from datetime import date

class Database:
	D = dict()
	def __init__(self):
			None

	def add(self, datestr, data):
			self.D[datestr] = data

class Transaction:
	def __init__(self, trstr):
		self.datastr = datestr
		self.date = date.fromisoformat(datestr)
		self.sender = 
		self.deposit = 
		self.withdraw = 
		
	def add(self, item, count):
		self.D[item] = count

	def print(self):
		print("Data (%s %s)"%(self.date, self.W[self.date.weekday()]))

				
for xlsf in glob.glob("*.xls"):
	csvf = xlsf.replace(".xls", ".csv")
	if (os.path.exists(csvf)):
		print(csvf)
	else:
		xls = pd.read_excel(xlsf)
		xls.to_csv(csvf)
		print("%s converted to %s"%(xlsf, csvf))

datastore = DataStore()
data = None
for csvf in glob.glob("*.csv"):
	with open(csvf, 'r') as csvfile:
		csvrd = csv.reader(csvfile, delimiter=',')
		for row in csvrd:
			print(row)
