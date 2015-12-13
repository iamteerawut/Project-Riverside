import River_Ayuthaya
import River_Bangsai
import River_Chainat
import River_Dowkanong
import River_Nakhonsawan
import River_Pamok
import River_Samlae
from nvd3 import lineChart

list_date_ay, list_do, list_ec, list_temp_ay, av_do, av_ec, av_temp = River_Ayuthaya.data_split()
list_date_bs, list_do, list_ec, list_temp_bs, av_do, av_ec, av_temp= River_Bangsai.data_split()
list_date_ch, list_do, list_ec, list_temp_ch, av_do, av_ec, av_temp = River_Chainat.data_split()
list_date_dk, list_do, list_ec, list_temp_dk, av_do, av_ec, av_temp = River_Dowkanong.data_split()
list_date_nk, list_do, list_ec, list_temp_nk, av_do, av_ec, av_temp = River_Nakhonsawan.data_split()
list_date_pm, list_do, list_ec, list_temp_pm, av_do, av_ec, av_temp = River_Pamok.data_split()
list_date_sl, list_do, list_ec, list_temp_sl, av_do, av_ec, av_temp = River_Samlae.data_split()

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

### Chart temp Ayuthaya
list_mean_temp_in_aday = average_per_day(list_temp_ay, list_date_ay)
output_file = open("Temp-Ayuthaya.html", "w")
chart = lineChart(name="lineChart Ayuthaya Temp", width=1244)
temp = range(1, 32)
july = list_mean_temp_in_aday[:31]
aug = list_mean_temp_in_aday[31:62]
sep = list_mean_temp_in_aday[62:]

chart.add_serie(y=july, x=temp, name='ก.ค.')
chart.add_serie(y=aug, x=temp, name='ส.ค.')
chart.add_serie(y=sep, x=temp, name='ก.ย.')
chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()

### Chart temp Bangsai
list_mean_do_in_aday = average_per_day(list_temp_bs, list_date_bs)
output_file = open("Temp-Bangsai.html", "w")
chart = lineChart(name="lineChart Bangsai Temp", width=1244)
temp = range(1, 32)
apr = list_mean_do_in_aday[:30]
may = list_mean_do_in_aday[30:61]
june = list_mean_do_in_aday[61:91]
july = list_mean_do_in_aday[91:122]
aug = list_mean_do_in_aday[122:153]
sep = list_mean_do_in_aday[153:]
    
chart.add_serie(y=apr, x=temp, name='เม.ย.')
chart.add_serie(y=may, x=temp, name='พ.ค.')
chart.add_serie(y=june, x=temp, name='มิ.ย.')
chart.add_serie(y=july, x=temp, name='ก.ค.')
chart.add_serie(y=aug, x=temp, name='ส.ค.')
chart.add_serie(y=sep, x=temp, name='ก.ย.')

chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()

### Chart temp Chainat
list_mean_do_in_aday = average_per_day(list_temp_ch, list_date_ch)
output_file = open("Temp-Chainat.html", "w")
chart = lineChart(name="lineChart Chainat Temp", width=1244)
temp = range(1, 32)
apr = list_mean_do_in_aday[:30]
may = list_mean_do_in_aday[30:61]
june = list_mean_do_in_aday[61:91]
july = list_mean_do_in_aday[91:122]
aug = list_mean_do_in_aday[122:153]
sep = list_mean_do_in_aday[153:]
    
chart.add_serie(y=apr, x=temp, name='เม.ย.')
chart.add_serie(y=may, x=temp, name='พ.ค.')
chart.add_serie(y=june, x=temp, name='มิ.ย.')
chart.add_serie(y=july, x=temp, name='ก.ค.')
chart.add_serie(y=aug, x=temp, name='ส.ค.')
chart.add_serie(y=sep, x=temp, name='ก.ย.')

chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()

### Chart temp Dowkanong
list_mean_temp_in_aday = average_per_day(list_temp_dk, list_date_dk)
output_file = open("Temp-Dowkanong.html", "w")
chart = lineChart(name="lineChart Dowkanong Temp", width=1244)
temp = range(1, 32)
temp2 = range(14, 32)
temp3 = range(1, 26)
july = list_mean_temp_in_aday[0:18]
aug = list_mean_temp_in_aday[18:43]
sep = list_mean_temp_in_aday[43:]

chart.add_serie(y=july, x=temp2, name='ก.ค.')
chart.add_serie(y=aug, x=temp3, name='ส.ค.')
chart.add_serie(y=sep, x=temp, name='ก.ย.')
chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()

### Chart temp Nakhonsawan
list_mean_do_in_aday = average_per_day(list_temp_nk, list_date_nk)
output_file = open("Temp-Nakhonsawan.html", "w")
chart = lineChart(name="lineChart Nakhonsawan Temp", width=1244)
temp = range(1, 32)
temp2 = range(23, 32)
apr = list_mean_do_in_aday[:30]
may = list_mean_do_in_aday[8:38]
june = list_mean_do_in_aday[38:68]
july = list_mean_do_in_aday[68:99]
aug = list_mean_do_in_aday[99:129]
sep = list_mean_do_in_aday[129:158]

chart.add_serie(y=apr, x=temp, name='เม.ย.')
chart.add_serie(y=may, x=temp, name='พ.ค.')
chart.add_serie(y=june, x=temp, name='มิ.ย.')
chart.add_serie(y=july, x=temp, name='ก.ค.')
chart.add_serie(y=aug, x=temp, name='ส.ค.')
chart.add_serie(y=sep, x=temp, name='ก.ย.')

chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()

### Chart temp Pamok
list_mean_do_in_aday = average_per_day_pm(list_temp_pm, list_date_pm)
output_file = open("Temp-Pamok.html", "w")
chart = lineChart(name="lineChart Pamok Temp", width=1244)
temp = range(1, 32)
apr = list_mean_do_in_aday[:30]
may = list_mean_do_in_aday[30:61]
june = list_mean_do_in_aday[61:91]
july = list_mean_do_in_aday[91:122]
aug = list_mean_do_in_aday[122:153]
sep = list_mean_do_in_aday[153:]

chart.add_serie(y=apr, x=temp, name='เม.ย.')
chart.add_serie(y=may, x=temp, name='พ.ค.')
chart.add_serie(y=june, x=temp, name='มิ.ย.')
chart.add_serie(y=july, x=temp, name='ก.ค.')
chart.add_serie(y=aug, x=temp, name='ส.ค.')
chart.add_serie(y=sep, x=temp, name='ก.ย.')

chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()

### Chart temp Samlae
list_mean_do_in_aday = average_per_day(list_temp_sl, list_date_sl)
output_file = open("Temp-Samlae.html", "w")
chart = lineChart(name="lineChart Samlae Temp", width=1244)
temp = range(1, 32)
temp2 = range(1, 14)
temp3 = range(17, 32)
temp4 = range(1, 26)
temp5 = range(1, 24)
apr = list_mean_do_in_aday[:30]
may = list_mean_do_in_aday[30:43]
july = list_mean_do_in_aday[43:57]
aug = list_mean_do_in_aday[57:82]
sep = list_mean_do_in_aday[82:105]

chart.add_serie(y=apr, x=temp, name='เม.ย.')
chart.add_serie(y=may, x=temp2, name='พ.ค.')
chart.add_serie(y=july, x=temp3, name='ก.ค.')
chart.add_serie(y=aug, x=temp4, name='ส.ค.')
chart.add_serie(y=sep, x=temp5, name='ก.ย.')

chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()
