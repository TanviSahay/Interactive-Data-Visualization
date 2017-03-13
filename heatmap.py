import csv
import os, re
import numpy

fb_data_path = './dataset_Facebook-table.csv'

Pagelikes    = []
PostTR       = []
PostTI       = []
EngagedU     = []
PostCons     = []
PostConp     = []
Conslikepage = []
Reaclikepage = []
likenengage  = []

os.remove('heatmap.csv')

heatmap_file = open('heatmap.csv','w')
heatmap = csv.writer(heatmap_file, delimiter = ',')

fb_file = open(fb_data_path,'rU')
fb_data = csv.reader(fb_file, dialect = csv.excel_tab)
for row in fb_data:
    if re.match('Page .*',row[0]):
        row_new = row[0].split(',')
        row_enter = [row_new[0],row_new[7],row_new[8],row_new[9],row_new[10],row_new[11],row_new[12],row_new[13],row_new[14]]  
        heatmap.writerow(row_enter)
        heatmap_file.close()
        
    if not re.match('Page .*',row[0]):
        row = row[0].split(',')
        #print row
        Pagelikes.append(row[0])
        PostTR.append((row[0],row[7]))
        PostTI.append((row[0],row[8]))
        EngagedU.append((row[0],row[9]))
        PostCons.append((row[0],row[10]))
        PostConp.append((row[0],row[11]))
        Conslikepage.append((row[0],row[12]))
        Reaclikepage.append((row[0],row[13]))
        likenengage.append((row[0],row[14]))

TotalLikes = {x for x in Pagelikes}
print TotalLikes

heatmap_file = open('heatmap.csv','a')
heatmap = csv.writer(heatmap_file, delimiter = ',')

for page in TotalLikes:
    new_row = []
    new_row.append(int(page))
    col1 = 0;
    col2 = 0;
    col3 = 0;
    col4 = 0;
    col5 = 0;
    col6 = 0;
    col7 = 0;
    col8 = 0;    
    for elem in PostTR:
        if elem[0] == page: col1 += int(elem[1])
    new_row.append(col1) 
    for elem in PostTI:
        if elem[0] == page: col2 += int(elem[1])
    new_row.append(col2) 
    for elem in EngagedU:
        if elem[0] == page: col3 += int(elem[1]) 
    new_row.append(col3)
    for elem in PostCons:
        if elem[0] == page: col4 += int(elem[1])
    new_row.append(col4) 
    for elem in PostConp:
        if elem[0] == page: col5 += int(elem[1])
    new_row.append(col5) 
    for elem in Conslikepage:
        if elem[0] == page: col6 += int(elem[1])
    new_row.append(col6) 
    for elem in Reaclikepage:
        if elem[0] == page: col7 += int(elem[1])
    new_row.append(col7) 
    for elem in likenengage:
        if elem[0] == page: col8 += int(elem[1]) 
    new_row.append(col8)

    heatmap.writerow(new_row)

heatmap_file.close()
