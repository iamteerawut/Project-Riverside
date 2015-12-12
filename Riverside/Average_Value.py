import River_Ayuthaya
import River_Bangsai
import River_Chainat
import River_Dowkanong
import River_Nakhonsawan
import River_Pamok
import River_Samlae
from nvd3 import lineChart

list_date, list_do, list_ec, list_temp, ave_do_ayuthaya, ave_ec_ayuthaya, ave_temp_ayuthaya = River_Ayuthaya.data_split()
list_date, list_do, list_ec, list_temp, ave_do_bangsai, ave_ec_bangsai, ave_temp_bangsai = River_Bangsai.data_split()
list_date, list_do, list_ec, list_temp, ave_do_chainat, ave_ec_chainat, ave_temp_chainat = River_Chainat.data_split()
list_date, list_do, list_ec, list_temp, ave_do_dowkanong, ave_ec_dowkanong, ave_temp_dowkanong = River_Dowkanong.data_split()
list_date, list_do, list_ec, list_temp, ave_do_nakhonsawan, ave_ec_nakhonsawan, ave_temp_nakhonsawan = River_Nakhonsawan.data_split()
list_date, list_do, list_ec, list_temp, ave_do_pamok, ave_ec_pamok, ave_temp_pamok = River_Pamok.data_split()
list_date, list_do, list_ec, list_temp, ave_do_samlae, ave_ec_samlae, ave_temp_samlae = River_Samlae.data_split()
#print(ave_do_ayuthaya, ave_do_bangsai, ave_do_chainat, ave_do_dowkanong, ave_do_nakhonsawan, ave_do_pamok, ave_do_samlae)
all_ave_do = [ave_do_ayuthaya, ave_do_bangsai, ave_do_chainat, ave_do_dowkanong, ave_do_nakhonsawan, ave_do_pamok, ave_do_samlae]
all_ave_ec = [ave_ec_ayuthaya, ave_ec_bangsai, ave_ec_chainat, ave_ec_dowkanong, ave_ec_nakhonsawan, ave_ec_pamok, ave_ec_samlae]
all_ave_temp = [ave_temp_ayuthaya, ave_temp_bangsai, ave_temp_chainat, ave_temp_dowkanong, ave_temp_nakhonsawan, ave_temp_pamok, ave_temp_samlae]

#created HTML
def ave_do_chart():
    output_file = open('Average-DO.html', 'w')
    chart = lineChart(name="lineChart of average D.O.", width=1244)
    xdata = range(9)
    ydata = all_ave_do

    extra_serie = {"tooltip": {"y_start": "There are", "y_end": " calls"}}
    chart.add_serie(y=ydata, x=xdata, name='D.O.', extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()

ave_do_chart()


#created HTML for average E.C.
def ave_ec_chart():
    output_file = open('Average-EC.html', 'w')
    chart = lineChart(name="lineChart of average E.C.", width=1244)
    xdata = range(9)
    ydata = all_ave_ec

    extra_serie = {"tooltip": {"y_start": "There are", "y_end": " calls"}}
    chart.add_serie(y=ydata, x=xdata, name='E.C.', extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()

ave_ec_chart()

#created HTML for average temperature
def ave_temp_chart():
    output_file = open('Average-Temp.html', 'w')
    chart = lineChart(name="lineChart of average Temperature", width=1244)
    xdata = range(9)
    ydata = all_ave_temp

    extra_serie = {"tooltip": {"y_start": "There are", "y_end": " calls"}}
    chart.add_serie(y=ydata, x=xdata, name='Temperature', extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()

ave_temp_chart()
