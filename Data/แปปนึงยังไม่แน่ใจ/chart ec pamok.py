import riverside_pamok
from nvd3 import lineChart

def pamok():
    """ """
    list_date, list_do, list_ec, list_temp, ave_do_pamok, ave_ec_pamok, ave_temp_pamok = riverside_pamok.data_split()
    list_mean_ec_in_aday = average_per_day(list_ec, list_date)

    #created HTML
    output_file = open('Chart mean EC in a day of Pamok.html', 'w')
    chart = lineChart(name="lineChart Pamok E.C.", width = 1244)
    xdata = range(1, 32)
    ydata1 = list_mean_ec_in_aday[:30]
    ydata2 = list_mean_ec_in_aday[30:61]
    ydata3 = list_mean_ec_in_aday[61:91]
    ydata4 = list_mean_ec_in_aday[91:122]
    ydata5 = list_mean_ec_in_aday[122:153]
    ydata6 = list_mean_ec_in_aday[153:]

    chart.add_serie(y=ydata1, x=xdata, name='เม.ย.')
    chart.add_serie(y=ydata2, x=xdata, name='พ.ค.')
    chart.add_serie(y=ydata3, x=xdata, name='มิ.ย.')
    chart.add_serie(y=ydata4, x=xdata, name='ก.ค.')
    chart.add_serie(y=ydata5, x=xdata, name='ส.ค.')
    chart.add_serie(y=ydata6, x=xdata, name='ก.ย.')
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()
    
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

pamok()
