import csv
def project_um():
    with open('Pamok.csv') as csvfile:
        test = csv.reader(csvfile)
        date = []
        value1 = []
        value2 = []
        value3 = []
        value4 = []
        value5 = []
        for i in csvfile:
            data = i.split(',')
            date.append(data[1])
            value1.append(data[2])
            value2.append(data[3])
            value3.append(data[4])
            value4.append(data[5])
            value5.append(data[6])

    return value1[0], value2[0], value3[0], value4[0], value5[0]
    
print(project_um())
