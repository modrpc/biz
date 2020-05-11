#!/opt/anaconda3/bin/python3

import pandas as pd
import glob, os
import csv
import datetime
from datetime import date

class Account:
	def __init__(self):
		self._db = dict()
		self._balance = 0
		None

	def deposit(self, datetime, typ, who, amount):
		self._balance = self._balance + amount

	def withdraw(self, datatime, typ, who, amount):
		self._balance = self._balance - amount

	def balance(self):
		return self._balance

class Transaction:
	def __init__(self, xact):
		#self.date = date.fromisoformat(datestr)
		self.sender = None
		self.deposit = None
		self.withdraw = None
		
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

acct = Account()
data = None
for csvf in glob.glob("*2020-03.csv"):
	with open(csvf, 'r') as csvfile:
		csvrd = csv.reader(csvfile, delimiter=',')
		for row in csvrd:
			dt = datetime.datetime.strptime(row[2], "%Y.%m.%d %H:%M:%S")
			typ = row[3]
			who = row[4]
			withdraw = int(row[5])
			deposit = int(row[6])
			if (withdraw != 0):
				acct.withdraw(dt, typ, who, withdraw)
			elif (deposit != 0):
				acct.deposit(dt, typ, who, deposit)
			print("%s %s with=%d dep=%d"%(typ, who, withdraw, deposit))
			print(acct.balance())
			
