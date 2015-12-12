import csv
from nvd3 import lineChart
def data_split():
    with open('Data/Chainat.csv', encoding="utf-8") as csvfile:
        test = csv.reader(csvfile)
        list_date = []
        list_do = []
        for i in test:
            data = i[0].split(';')
            list_date.append(data[2])
            list_do.append(data[4])
    list_do = change_value_to_float(list_do)
    list_mean_do_in_aday = average_per_day(list_do, list_date)
    
    #created HTML
    output_file = open('DO-Chainat.html', 'w')
    chart = lineChart(name="lineChart Chainat DO", width=1244)
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
    
def change_value_to_float(valu):
    list_value = []
    loop = 0
    for i in valu:
        value = i[1:len(valu[loop])-1]
        if value != 'F':
            value = float(value)
        list_value.append(value)
        loop += 1
    return list_value

def average_per_day(valu, date):
    
    list_average = []
    list_date = []
    for i in date:
        day = i.split()
        list_date.append(int(day[0][1:]))
    # fix constant
    cons = 1
    aver = 0
    time = 0
    for i in range(len(list_date)):
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
