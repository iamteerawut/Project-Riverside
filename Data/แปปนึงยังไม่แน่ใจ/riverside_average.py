import riverside_ayuthaya
import riverside_bangsai
import riverside_chainat
import riverside_dowkanong
import riverside_nakhonsawan
import riverside_pamok
import riverside_samlae
from nvd3 import discreteBarChart

list_date, list_do, list_ec, list_temp, ave_do_ayuthaya, ave_ec_ayuthaya, ave_temp_ayuthaya = riverside_ayuthaya.data_split()
list_date, list_do, list_ec, list_temp, ave_do_bangsai, ave_ec_bangsai, ave_temp_bangsai = riverside_bangsai.data_split()
list_date, list_do, list_ec, list_temp, ave_do_chainat, ave_ec_chainat, ave_temp_chainat = riverside_chainat.data_split()
list_date, list_do, list_ec, list_temp, ave_do_dowkanong, ave_ec_dowkanong, ave_temp_dowkanong = riverside_dowkanong.data_split()
list_date, list_do, list_ec, list_temp, ave_do_nakhonsawan, ave_ec_nakhonsawan, ave_temp_nakhonsawan = riverside_nakhonsawan.data_split()
list_date, list_do, list_ec, list_temp, ave_do_pamok, ave_ec_pamok, ave_temp_pamok = riverside_pamok.data_split()
list_date, list_do, list_ec, list_temp, ave_do_samlae, ave_ec_samlae, ave_temp_samlae = riverside_samlae.data_split()
#print(ave_do_ayuthaya, ave_do_bangsai, ave_do_chainat, ave_do_dowkanong, ave_do_nakhonsawan, ave_do_pamok, ave_do_samlae)
all_ave_do = [ave_do_ayuthaya, ave_do_bangsai, ave_do_chainat, ave_do_dowkanong, ave_do_nakhonsawan, ave_do_pamok, ave_do_samlae]
all_ave_ec = [ave_ec_ayuthaya, ave_ec_bangsai, ave_ec_chainat, ave_ec_dowkanong, ave_ec_nakhonsawan, ave_ec_pamok, ave_ec_samlae]
all_ave_temp = [ave_temp_ayuthaya, ave_temp_bangsai, ave_temp_chainat, ave_temp_dowkanong, ave_temp_nakhonsawan, ave_temp_pamok, ave_temp_samlae]

#created HTML
def ave_do_chart():
    output_file = open('ave_do_chart.html', 'w')
    chart = discreteBarChart(name='discreteBarChart of average D.O.', height=700, width=700)

    xdata = ["Ayuthaya", "Bangsai", "Chainat", "Dowkanong", "Nakhonsawan", "Pamok", "Samlea"]
    ydata = all_ave_do

    extra_serie = {"tooltip": {"y_start": "", "y_end": "m/L"}}
    chart.add_serie(y=ydata, x=xdata, name='D.O.', extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()

ave_do_chart()


#created HTML for average E.C.
def ave_ec_chart():
    output_file = open('ave_ec_chart.html', 'w')
    chart = discreteBarChart(name="lineChart of average E.C.", width=1244)
    xdata = ["Ayuthaya", "Bangsai", "Chainat", "Dowkanong", "Nakhonsawan", "Pamok", "Samlea"]
    ydata = all_ave_ec

    extra_serie = {"tooltip": {"y_start": "", "y_end": " m"}}
    chart.add_serie(y=ydata, x=xdata, name='E.C.', extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()

ave_ec_chart()

#created HTML for average temperature
def ave_temp_chart():
    output_file = open('ave_temp_chart.html', 'w')
    chart = discreteBarChart(name="lineChart of average Temperature", width=1244)
    xdata = ["Ayuthaya", "Bangsai", "Chainat", "Dowkanong", "Nakhonsawan", "Pamok", "Samlea"]
    ydata = all_ave_temp

    extra_serie = {"tooltip": {"y_start": "", "y_end": " C"}}
    chart.add_serie(y=ydata, x=xdata, name='Temperature', extra=extra_serie)
    chart.buildhtml()
    output_file.write(chart.htmlcontent)
    # close Html file
    output_file.close()

ave_temp_chart()
