#!/opt/anaconda3/bin/python3

import sys
import os
import glob
import csv
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




def build_date_sales_lists(csvfs):
	dateL = []
	salesL = []
	for csvf in csvfs:
		with open(csvf, 'r') as csvfile:
			sales = []
			date = None
			rowcnt = 0

			csvrd = csv.reader(csvfile, delimiter=',')
			datestr = csvf.replace("/06", "").replace(".csv", "")
			date = pd.to_datetime(datestr)
			dateL.append(date)

			for row in csvrd:
				rowcnt = rowcnt + 1
				if (rowcnt < 4): continue
				if (row[2] == "합  계"): continue
				sales.append([row[2], int(row[4].replace(',', ''))])
			salesL.append(sales)

	return (dateL, salesL)


def is_weekday(pdt):
	return pdt.day_name() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_weekend(pdt):
	return pdt.day_name() in ['Saturday', 'Sunday']

def run(dir):
	csvfs = build_csv(dir)
	(dateL, salesL) = build_date_sales_lists(csvfs)
	dateNDA = pd.DataFrame(dateL)
	salesNDA = pd.DataFrame(salesL)

	print(dateNDA)

	d61 = pd.to_datetime("2020-06-01")
	#print(d61.day_name())
	#print(salesNDA[dateNDA == d61])

	#for sales in salesL:
	#print(sales['단팥빵'])

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: " + sys.argv[0] + " <dir>")
		quit()
	run(sys.argv[1])
