#!/opt/anaconda3/bin/python3

import sys
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

datastore = DataStore()
data = None

def build_csv(dir):
	for xlsf in glob.glob(dir + "*"):
		csvf = xlsf.replace(".xls", ".csv")
		if (os.path.exists(csvf)):
			print(csvf)
		else:
			xls = pd.read_excel(xlsf)
			xls.to_csv(csvf)
			print("%s converted to %s"%(xlsf, csvf))


def build_dates(dir):
	for csvf in glob.glob(dir + "/*.csv"):
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

def build_data(dir):
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

def run(dir):
	build_csv(dir)
	build_dates(dir)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: " + sys.argv[0] + " <dir>")
		quit()
	run(sys.argv[1])
