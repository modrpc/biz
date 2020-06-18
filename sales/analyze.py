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
		self.sorted_list = None

	def add(self, item):
		if item in self.dict:
			return
		self.dict[item] = 0

	def is_valid(self, item):
		if item in self.dict:
			return True
		else:
			return False

	def list(self):
		if self.sorted_list == None:
			self.sorted_list = sorted(self.dict.keys())
			nitems = 0
			for item in self.sorted_list:
				self.dict[ltem] = nitems
				nitems = nitems + 1
		return self.sorted_list

	def size(self):
		return len(self.list())

	def item_index(self, name):
		return self.dict[name]


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

def build_sales_list(sales):
	ilst = [0 for _ in range(items.size())]
	for sale in sales:
		ilst[items.item_index(sale[0])] = int(sale[1])
	return ilst
	

def build_sales_dataframe(csvpaths):
	global items
	datesL = []
	itemsL = []
	salesData = []
	for csvpath in csvpaths:
		with open(csvpath, 'r') as csvfile:
			nrow = 0
			csvrd = csv.reader(csvfile, delimiter=',')
			datesL.append(csvpath.replace('/06', '').replace('.csv', ''))

			for row in csvrd:
				nrow = nrow + 1
				if nrow < 4 or row[2] == '합  계': continue
				items.add(row[2])

	for csvpath in csvpaths:
		print(csvpath)
		with open(csvpath, 'r') as csvfile:
			salesL = []
			csvrd = csv.reader(csvfile, delimiter=',')
			for row in csvrd:
				if (items.is_valid(row[2])):
					salesL.append([row[2], row[4]])
					print(row)
					print(row[2], row[4])
			lst = build_sales_list(salesL)
			salesData.append(lst)

	dateIdx = pd.to_datetime(datesL)
	return pd.DataFrame(data=salesData, index=dateIdx, columns=items.list())

def is_weekday(pdt):
	return pdt.day_name() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_weekend(pdt):
	return pdt.day_name() in ['Saturday', 'Sunday']

salesDF = None
def run(dir):
	global salesDF
	csvpaths = build_csv_paths(dir)
	salesDF = build_sales_dataframe(csvpaths)
	print(salesDF)

if __name__ == '__main__':
	if (len(sys.argv) < 2):
		print('Usage: ' + sys.argv[0] + ' <dir>')
		quit()
	run(sys.argv[1])
