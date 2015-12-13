import River_Ayuthaya
import River_Bangsai
import River_Chainat
import River_Dowkanong
import River_Nakhonsawan
import River_Pamok
import River_Samlae
from nvd3 import lineChart

list_date_ay, list_do, list_ec_ay, list_temp_ay, av_do, av_ec, av_temp = River_Ayuthaya.data_split()
list_date_bs, list_do, list_ec_bs, list_temp_bs, av_do, av_ec, av_temp= River_Bangsai.data_split()
list_date_ch, list_do, list_ec_ch, list_temp_ch, av_do, av_ec, av_temp = River_Chainat.data_split()
list_date_dk, list_do, list_ec_dk, list_temp_dk, av_do, av_ec, av_temp = River_Dowkanong.data_split()
list_date_nk, list_do, list_ec_nk, list_temp_nk, av_do, av_ec, av_temp = River_Nakhonsawan.data_split()
list_date_pm, list_do, list_ec_pm, list_temp_pm, av_do, av_ec, av_temp = River_Pamok.data_split()
list_date_sl, list_do, list_ec_sl, list_temp_sl, av_do, av_ec, av_temp = River_Samlae.data_split()
    
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

def average_per_day_pm(valu, date):  
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

#created Ayuthaya EC HTML
list_mean_ec_in_aday = average_per_day(list_ec_ay, list_date_ay)
output_file = open('EC-Ayuthaya.html', 'w')
chart = lineChart(name="lineChart Ayuthaya E.C.", width = 1244)
xdata = range(1, 32)
ydata4 = list_mean_ec_in_aday[:31]
ydata5 = list_mean_ec_in_aday[31:62]
ydata6 = list_mean_ec_in_aday[62:]

chart.add_serie(y=ydata4, x=xdata, name='ก.ค.')
chart.add_serie(y=ydata5, x=xdata, name='ส.ค.')
chart.add_serie(y=ydata6, x=xdata, name='ก.ย.')
chart.buildhtml()
output_file.write(chart.htmlcontent)
#close Html file
output_file.close()

#created Bangsai EC HTML
list_mean_ec_in_aday = average_per_day(list_ec_bs, list_date_bs)
output_file = open('EC-Bangsai.html', 'w')
chart = lineChart(name="lineChart Bangsai E.C.", width=1244)
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

#close Html file
output_file.close()

#created Chainat EC HTML
list_mean_ec_in_aday = average_per_day(list_ec_ch, list_date_ch)
output_file = open('EC-Chainat.html', 'w')
chart = lineChart(name="lineChart Chainat E.C.", width=1244)
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

#close Html file
output_file.close()

#created Dowkanong EC HTML
list_mean_ec_in_aday = average_per_day(list_ec_dk, list_date_dk)
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

#close Html file
output_file.close()


#created Nakhonsawan EC HTML
list_mean_ec_in_aday = average_per_day(list_ec_nk, list_date_nk)
output_file = open('EC-Nakhonsawan.html', 'w')
chart = lineChart(name="lineChart Nakhonsawan E.C.", width = 1244)
xdata = range(1, 32)
xdata1 = range(23, 32)
ydata1 = list_mean_ec_in_aday[23:31]
ydata2 = list_mean_ec_in_aday[31:61]
ydata3 = list_mean_ec_in_aday[61:91]
ydata4 = list_mean_ec_in_aday[91:122]
ydata5 = list_mean_ec_in_aday[122:152]
ydata6 = list_mean_ec_in_aday[152:]

chart.add_serie(y=ydata1, x=xdata1, name='เม.ย.')
chart.add_serie(y=ydata2, x=xdata, name='พ.ค.')
chart.add_serie(y=ydata3, x=xdata, name='มิ.ย.')
chart.add_serie(y=ydata4, x=xdata, name='ก.ค.')
chart.add_serie(y=ydata5, x=xdata, name='ส.ค.')
chart.add_serie(y=ydata6, x=xdata, name='ก.ย.')
chart.buildhtml()
output_file.write(chart.htmlcontent)

#close Html file
output_file.close()


#created Pamok EC HTML
list_mean_ec_in_aday = average_per_day_pm(list_ec_pm, list_date_pm)
output_file = open('EC-Pamok.html', 'w')
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

#close Html file
output_file.close()


#created Pamok EC HTML
list_mean_ec_in_aday = average_per_day(list_ec_sl, list_date_sl)
output_file = open('EC-Samlae.html', 'w')
chart = lineChart(name="lineChart Samlae E.C.", width=1244)
xdata = range(1, 32)
xdata1 = range(17, 32)
ydata1 = list_mean_ec_in_aday[:30]
ydata2 = list_mean_ec_in_aday[30:43]
ydata4 = list_mean_ec_in_aday[43:57]
ydata5 = list_mean_ec_in_aday[57:82]
ydata6 = list_mean_ec_in_aday[82:]

chart.add_serie(y=ydata1, x=xdata, name='เม.ย.')
chart.add_serie(y=ydata2, x=xdata, name='พ.ค.')
chart.add_serie(y=ydata4, x=xdata1, name='ก.ค.')
chart.add_serie(y=ydata5, x=xdata, name='ส.ค.')
chart.add_serie(y=ydata6, x=xdata, name='ก.ย.')
chart.buildhtml()
output_file.write(chart.htmlcontent)

# close Html file
output_file.close()
