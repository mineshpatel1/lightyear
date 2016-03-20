#!/usr/bin/python

# Load Google Analytics dimensions based on TSV file
import lyf
import csv

from lyf import *
from datetime import date, timedelta, datetime	# Date time
from dateutil.parser import parse	# Date parser

def main():

	# Read TSV file, looping through dimensions
	i = 0
	with open(lyf.get_config('ETL', 'GA_Dims'), 'r') as f:
		f = csv.reader(f, delimiter='\t')
		for row in f:
			if (i > 0):
				table = row[0]
				ga_dims = row[1].split(',')
				columns = row[2].split(',')
				keys = row[3].split(',')
				sql.load_ga_dim(False, table, ga_dims, columns, keys)
			i += 1
			
if __name__ == '__main__':
	main()