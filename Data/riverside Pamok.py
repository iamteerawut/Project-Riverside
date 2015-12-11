import csv
from pylab import *
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
        hist(value1, range=[0,10], bins=10)
        xlabel = ('Date')
        ylabel = ('D.O. value')
        grid(Ture)
        xlim(0,10)
        ylim(0,5)
        show()
   
print(project_um())
