from nvd3 import stackedAreaChart

output_file = open('test-nvd3.html', 'w')

chart = stackedAreaChart(name='stackedAreaChart', height=400, width=400)

xdata = [100, 101, 102, 103, 104, 105, 106,]
ydata = [6, 11, 12, 7, 11, 10, 11]

extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
chart.add_serie(name="Serie 1", y=ydata, x=xdata, extra=extra_serie)
chart.buildhtml()
output_file.write(chart.htmlcontent)


output_file.close()
