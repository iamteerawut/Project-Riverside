import csv
from nvd3 import lineChart
def project_um():
    with open('Bangsai.csv', encoding="utf-8") as csvfile:
        test = csv.reader(csvfile)
        list_date = []
        list_do = []
        list_ec = []
        list_temp = []
        for i in test:
            data = i[0].split(';')
            list_date.append(data[1])
            list_do.append(data[2])
            list_ec.append(data[3])
            list_temp.append(data[4])
    list_do = change_value_to_float(list_do)
    list_ec = change_value_to_float(list_ec)
    list_temp = change_value_to_float(list_temp)
    return len(list_do)
    #created HTML
    #chart = lineChart(name="lineChart", x_is_date=True, 

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

print(project_um())


##เก็บค่าของแต่ละ value ไว้ในลิสต์ของแต่ละค่า
#แก้ชื่อตัวแปรน่ะ
#do = ปริมาณออกซิเจนที่ละลายในน้ำ ค่าเป็นเลขหลักเดียวกับทศนิยม เช่น 5.8, 6.4
#ec = ค่าความนำไฟฟ้า ค่าส่วนใหญ่เป็นเลขสามหลักกับทศนิยม เช่น 148.3, 154.5
#temp = อุณภูมิน้ำ ค่าส่วนใหญ่เป็นเลขสองหลักกับทศนิยม เช่น 19.5, 33.0
