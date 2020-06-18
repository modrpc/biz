#!/opt/anaconda3/bin/python3

import sys
import os
import glob
import csv
import numpy as np
import pandas as pd

class Items:
	def __init__(self):
		self.dict = {}
		self.sorted = False
		self.sorted_list = None

	def add(self, item):
		if item in self.dict:
			return
		self.dict[item] = 0

	def list(self):
		if not sorted:
			self.sorted_list = sorted(self.dict.keys())
			nitems = 0
			for item in sorted_list:
				self.dict[item] = nitems
				nitems = nitems + 1
		return self.sorted_list

	def size(self):
		return len(self.list())


items = Items()

def build_csv_paths(dir):
	csvpaths = []
	for xlspath in glob.glob(dir + '/*.xls'):
		csvpath = xlspath.replace('.xls', '.csv')
		csvpaths.append(csvpath)
		if (os.path.exists(csvpath)):
			continue
		else:
			xls = pd.read_excel(xlspath)
			xls.to_csv(csvpath)
			print('%s converted to %s'%(xlspath, csvpath))
	return csvpaths

def build_sorted_item_list(salesL):
	itemD = {}
	for sales in salesL:
		for item in sales:
			if item[0] in itemD:
				continue
			itemD[item[0]] = 0
			print(item[0])

def build_sales_data(items)

def build_sales_dataframe(csvpaths):
	global items
	datesL = []
	salesL = []
	itemsL = []
	for csvpath in csvpaths:
		with open(csvpath, 'r') as csvfile:
			salesD = {}
			nrow = 0

			csvrd = csv.reader(csvfile, delimiter=',')
			datesL.append(csvpath.replace('/06', '').replace('.csv', ''))

			for row in csvrd:
				nrow = nrow + 1
				if nrow < 4 or row[2] == '합  계': continue
				
				salesD[row[2]] = int(row[4])
				items.add(row[2])
			salesDF = pd.DataFrame(pd.Series(salesD))
			salesL.append(salesDF)

	dateIdx = pd.to_datetime(datesL)
	return pd.DataFrame(data=salesL, index=dateIdx, columns=items.list())

def is_weekday(pdt):
	return pdt.day_name() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_weekend(pdt):
	return pdt.day_name() in ['Saturday', 'Sunday']

def run(dir):
	csvpaths = build_csv_paths(dir)
	salesDF = build_sales_dataframe(csvpaths)

	print(salesDF.index)
	print(salesDF.columns)
	print(salesDF['단팥빵'])
	#print(salesDF[pd.to_datetime('2020-06-01')]['단팥빵'])

if __name__ == '__main__':
	if (len(sys.argv) < 2):
		print('Usage: ' + sys.argv[0] + ' <dir>')
		quit()
	run(sys.argv[1])
