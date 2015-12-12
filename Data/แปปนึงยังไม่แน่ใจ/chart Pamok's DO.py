import csv
from nvd3 import lineChart
def data_split():
    with open('Pamok.csv') as csvfile:
        test = csv.reader(csvfile)
        list_date = []
        list_do = []
        for i in test:
            list_date.append(i[1])
            list_do.append(i[2])
    list_do = change_value_to_float(list_do)
    list_mean_do_in_aday = average_per_day(list_do, list_date)

   #created HTML
    output_file = open('Pamok.html', 'w')
    chart = lineChart(name="lineChart Pamok DO", width=1244)
    xdata = range(1, 32)
    ydata = list_mean_do_in_aday[:30]
    ydata2 = list_mean_do_in_aday[30:61]
    ydata3 = list_mean_do_in_aday[61:91]
    ydata4 = list_mean_do_in_aday[91:122]
    ydata5 = list_mean_do_in_aday[122:153]
    ydata6 = list_mean_do_in_aday[153:]
    
    chart.add_serie(y=ydata, x=xdata, name='เม.ย.')
    chart.add_serie(y=ydata2, x=xdata, name='พ.ค.')
    chart.add_serie(y=ydata3, x=xdata, name='มิ.ย.')
    chart.add_serie(y=ydata4, x=xdata, name='ก.ค.')
    chart.add_serie(y=ydata5, x=xdata, name='ส.ค.')
    chart.add_serie(y=ydata6, x=xdata, name='ก.ย.')
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()
    
def change_value_to_float(data):
    list_data = []
    for i in range(1, len(data)):
        if data[i] != 'F':
            data[i] = float(data[i])
        list_data.append(data[i])
    return list_data

def average_per_day(valu, date):
    list_average = []
    list_date = []
    for i in date:
        day = i.split()
        list_date.append(int(day[0]))
    # fix constant
    cons = list_date[0]
    aver = 0
    time = 0
    for i in range(len(valu)):
        if list_date[i] == cons:
            if valu[i] == 'F':
                pass
            else:
                aver += float(valu[i])
                time += 1
        elif list_date[i] != cons:
            list_average.append('%.2f'%(aver/time))
            cons = list_date[i]
            if valu[i] == 'F':
                pass
            else:
                aver = float(valu[i])
                time = 1
    return list_average

data_split()
