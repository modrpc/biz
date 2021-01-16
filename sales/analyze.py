import sys
import pandas as pd

<<<<<<< HEAD
# DB store for sales data
class DataDB:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def build_db(self):
        
    
    
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

	def size(self):
		return len(self.sorted_list)

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
			self.dict[date] = np.add(self.dict[date], sales)

	def data(self):
		lst = [None for _ in range(self.dates.size())]
		for date in self.dict.keys():
			lst[self.dates.date_index(date)] = self.dict[date]
			
		return lst

		
dates = Dates()
items = Items()
sales = SalesData(dates, items)


# build a list of CSV files from DATA_DIR
DATA_DIR = 'data'
def build_csv_paths(dir):
	csvpaths = []
	for csvpath in glob.glob(DATA_DIR + '/*.csv'):
		csvpaths.append(csvpath)
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
			sales.add(date, lst)

	dateIdx = pd.to_datetime(dates.list())
	return pd.DataFrame(data=sales.data(), index=dateIdx, columns=items.list())

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
=======
import pathlib


def run(file):
    datadir = pathlib.Path('data/')
    path = datadir / (file + '.xlsx')
    df = pd.read_excel(path)
    print(df)
>>>>>>> 506e1411f33e9c302d7200b6a8b89e30c64e249c


def read_data_files():
    global DATA_DIR
        
    
def main():
    datafiles = read_data_files()
    

if __name__ == '__main__':
    print(os.getcwd())
    if (len(sys.argv) < 2):
        print('Usage: ' + sys.argv[0] + ' <filename>')
        sys.exit()
    run(sys.argv[1])
