#!/opt/anaconda3/bin/python3

import sys
import glob, os
import csv
import datetime
import numpy as np
import pandas as pd


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
		
	def add(self, item, count):
		self.D[item] = count

	def print(self):
		print("Data (%s %s)"%(self.date, self.W[self.date.weekday()]))

datastore = DataStore()
data = None

# @return list of paths of csv files
def build_csv(dir):
	csvfs = []
	for xlsf in glob.glob(dir + "/*.xls"):
		csvf = xlsf.replace(".xls", ".csv")
		print(xlsf)
		csvfs.append(csvf)
		if (os.path.exists(csvf)):
			continue
		else:
			xls = pd.read_excel(xlsf)
			xls.to_csv(csvf)
			print("%s converted to %s"%(xlsf, csvf))
	return csvfs


def build_db(csvfs):
	dateL = []
	salesL = []
	for csvf in csvfs:
		with open(csvf, 'r') as csvfile:
			sales = []
			date = None
			rowcnt = 0
			csvrd = csv.reader(csvfile, delimiter=',')
			datestr = csvf.replace("/06", "").replace(".csv", "")
			print(datestr)
			date = datetime.date.fromisoformat(datestr)
			dateL.append(date)
			for row in csvrd:
				rowcnt = rowcnt + 1
				if (rowcnt < 4): continue
				if (row[2] == "합  계"): continue
				sales.append([row[2], int(row[4].replace(',', ''))])
			salesL.append(sales)
	return (dateL, salesL)
					

def run(dir):
	csvfs = build_csv(dir)
	(dateL, salesL) = build_db(csvfs)
	print(dateL)
	print(salesL[0])
	dateNDA = np.array(dateL)
	salesNDA = np.array(salesL)
	print(salesNDA(dateNDA == datetime.date("2020-06-01")))

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: " + sys.argv[0] + " <dir>")
		quit()
	run(sys.argv[1])
