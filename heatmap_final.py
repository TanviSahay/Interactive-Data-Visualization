import csv
import os, re
import numpy

fb_data_path = './dataset_Facebook-table.csv'

os.remove('heatmap_type.csv')
#os.remove('heatmap_final.csv')
heatmap_file = open('heatmap_type.csv','w')
heatmap = csv.writer(heatmap_file, delimiter = ',')

fb_file = open(fb_data_path,'rU')
fb_data = csv.reader(fb_file, dialect = csv.excel_tab)

header = ['Page Total Likes','Type','Category','Post Month','Post Weekday','Post Hour','Paid','comment','like','share','Total Interactions', 'Features', 'Feature Value']
heatmap.writerow(header)

heatmap_file.close()

heatmap_file = open('heatmap_type.csv','a')
heatmap = csv.writer(heatmap_file, delimiter = ',')

for row in fb_data:
    if re.match('Page .*',row[0]):
        row_new = row[0].split(',')
        temp_dict = {}
        temp_dict['val1']    = row_new[7]
        temp_dict['val2']    = row_new[8]
        temp_dict['val3']    = row_new[9]
        temp_dict['val4']    = row_new[10]
        temp_dict['val5']    = row_new[11]
        temp_dict['val6']    = row_new[12]
        temp_dict['val7']    = row_new[13]
        temp_dict['val8']    = row_new[14]
 
    if not re.match('Page .*',row[0]):
        row = row[0].split(',')
        for i in range(1,9):
            index = 'val' + str(i)
            row_add = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[15],row[16],row[17],row[18],temp_dict[index],row[i+6]]
            heatmap.writerow(row_add)
heatmap_file.close()
'''
heatmap_file = open('heatmap.csv','rU')
heatmap = csv.reader(heatmap_file, dialect = csv.excel_tab)

totalLikes = []
for row in heatmap:
    row_new = row[0].split(',')
    totalLikes.append(row_new[0])

heatmap_file.close()
     
UniqueLikes    = {x for x in totalLikes}

heatmap_final_file = open('heatmap_final.csv','w')
heatmap_final      = csv.writer(heatmap_final_file, delimiter = ',')
heatmap_final.writerow(header)

heatmap_final_file.close()

heatmap_final_file = open('heatmap_final.csv','a')
heatmap_final      = csv.writer(heatmap_final_file, delimiter = ',')



for elem in UniqueLikes:
    for k in temp_dict.keys():
        heatmap_file = open('heatmap.csv','rU')
        heatmap = csv.reader(heatmap_file, dialect = csv.excel_tab)
        #print elem, temp_dict[k]
        count = 0
        for row in heatmap:
            #print '-------LOOP 1 ENTERED--------'
            row_new_2 = row[0].split(',')
            #print row_new_2
            #print '-----', row_new_2[0], row_new_2[1], row_new_2[2], '-----'
            if row_new_2[0] == elem and row_new_2[1] == temp_dict[k]: 
                print '-----PRINTING-----'
                count += int(row_new_2[2])
                print count
        row_add = [elem, temp_dict[k], count]
        heatmap_final.writerow(row_add)
        heatmap_file.close()

heatmap_final_file.close()
'''
