import River_Dowkanong
from nvd3 import lineChart

def dowkanong():
    """ """
    list_date, list_do, list_ec, list_temp, ave_do_dowkanong, ave_ec_dowkanong, ave_temp_dowkanong = River_Dowkanong.data_split()
    list_mean_ec_in_aday = average_per_day(list_ec, list_date)

    #created HTML
    output_file = open('EC-Dowkanong.html', 'w')
    chart = lineChart(name="lineChart Dowkanong E.C.", width = 1244)
    xdata = range(1, 32)
    ydata4 = list_mean_ec_in_aday[14:31]
    ydata5 = list_mean_ec_in_aday[31:56]
    ydata6 = list_mean_ec_in_aday[56:]

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
        list_date.append(int(day[0][1:]))
    # fix constant
    cons = list_date[0]
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

dowkanong()
