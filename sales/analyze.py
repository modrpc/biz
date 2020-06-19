#!/opt/anaconda3/bin/python3

import sys
import os
import glob
import csv
import numpy as np
import pandas as pd


class Dates:
	def __init__(self):
		self.dict = {}
		self.sorted_list = None

	def add(self, date):
		if date in self.dict:
			return
		self.dict[date] = 0

	def list(self):
		if self.sorted_list == None:
			self.sorted_list = sorted(self.dict.keys())
			ndates = 0
			for date in self.sorted_list:
				self.dict[date] = ndates
				ndates = ndates + 1
		return self.sorted_list

	def date_index(self, date):
		return self.dict[date]

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
				self.dict[item] = nitems
				nitems = nitems + 1
		return self.sorted_list

	def size(self):
		return len(self.list())

	def item_index(self, name):
		return self.dict[name]

class SalesData:
	def __init__(self, dates, items):
		self.dict = {}
		self.dates = dates
		self.items = items
		self.sorted_list = None

	def add(self, date, sales):
		if date not in self.dict.keys():
			self.dict[date] = sales
		else:
			self.dict[date] = numpy.add(self.dict[date], sales)

	def data(self):
		lst = []
		
		return 

		
dates = Dates()
items = Items()

def build_csv_paths(dir):
	csvpaths = []
	for idx in ['01', '02']:
		for xlspath in glob.glob(dir + '/' + idx + '/*.xls'):
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
	lst = [0 for _ in range(items.size())]
	for sale in sales:
		lst[items.item_index(sale[0])] = int(sale[1])
	return lst

def get_date_pos(csvpath):
	strs = csvpath.split('/')
	date = strs[1] + strs[3][2:].replace('.csv', '')
	pos = strs[2]
	return (date, pos)

def build_sales_dataframe(csvpaths):
	global dates
	global items
	salesData = []

	# 1) build the Items object, which contains all items sold 
	# 2) build the Dates object
	for csvpath in csvpaths:
		with open(csvpath, 'r') as csvfile:
			nrow = 0
			csvrd = csv.reader(csvfile, delimiter=',')
			(date, _) = get_date_pos(csvpath)
			dates.add(date)
			for row in csvrd:
				nrow = nrow + 1
				if nrow < 4 or row[2] == '합  계': continue
				items.add(row[2])

	# build sales matrix (row=date, column=items)
	for csvpath in csvpaths:
		with open(csvpath, 'r') as csvfile:
			salesL = []
			csvrd = csv.reader(csvfile, delimiter=',')
			(date, pos) = get_date_pos(csvpath)
			for row in csvrd:
				if (items.is_valid(row[2])):
					salesL.append([row[2], row[4]])
			lst = build_sales_list(salesL)
			salesData.append(lst)

	dateIdx = pd.to_datetime(dates.list())
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
