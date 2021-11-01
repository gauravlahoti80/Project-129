import csv

data = []

with open('dwarf_stars.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

header = data[0]
planet_data = data[1:]

for row in planet_data:
    if row[4] != '' and row[3] != '':
        row[4] = float(row[4]) * 0.102763
        row[3] = float(row[3]) * 0.000954588

with open('new.csv' , 'a+' , newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(planet_data)