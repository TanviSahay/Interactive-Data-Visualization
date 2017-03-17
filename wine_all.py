import os, csv
import re

wine_red_path   = './winequality-red.csv'
wine_white_path = './winequality-white.csv'

red_wine   = open(wine_red_path, 'rU')
white_wine = open(wine_white_path, 'rU')

red_wine_data = csv.reader(red_wine, dialect = csv.excel_tab)
white_wine_data = csv.reader(white_wine, dialect = csv.excel_tab)

wine_all_file = open('wine_all.csv','wb')
wine_all      = csv.writer(wine_all_file, delimiter = ',')

for row in red_wine_data:
    if re.match('fixed .*',row[0]): 
        header = ['Type']
    else:
        header = ['red']
    
    rows = row[0].split(',')
    header.extend(rows)
    wine_all.writerow(header)

for row in white_wine_data:
    if not re.match('fixed .*', row[0]):
        header = ['white']
        rows = row[0].split(',')
        header.extend(rows)
        wine_all.writerow(header)

print header 
