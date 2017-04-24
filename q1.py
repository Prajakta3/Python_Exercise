import csv

with open('FL_insurance_sample.csv', 'r') as old:
    read = csv.reader(old)
    list1 = []
    for data in read:
        list1.append(data)

old.close()
with open('new_file.csv','w') as new:
    write = csv.writer(new)
    for a in list1:
        write.writerow(a[2:18:3])
new.close()