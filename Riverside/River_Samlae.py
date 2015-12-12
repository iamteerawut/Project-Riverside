import csv
def data_split():
    with open('Data/Samlae.csv', encoding="utf-8") as csvfile:
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
    average_do = sol_average(list_do)
    average_ec = sol_average(list_ec)
    average_temp = sol_average(list_temp)
    return list_date, list_do, list_ec, list_temp, average_do, average_ec, average_temp

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


##เก็บค่าของแต่ละ value ไว้ในลิสต์ของแต่ละค่า
#แก้ชื่อตัวแปรน่ะ
#do = ปริมาณออกซิเจนที่ละลายในน้ำ ค่าเป็นเลขหลักเดียวกับทศนิยม เช่น 5.8, 6.4
#ec = ค่าความนำไฟฟ้า ค่าส่วนใหญ่เป็นเลขสามหลักกับทศนิยม เช่น 148.3, 154.5
#temp = อุณภูมิน้ำ ค่าส่วนใหญ่เป็นเลขสองหลักกับทศนิยม เช่น 19.5, 33.0

#nanntch edit for find average of 'do', 'ec' and 'temp' @2015.12.11
def sol_average(lis):
    total, count_f = 0, 0
    for num in lis:
        if num != "F":
            total += num
        else:
            count_f += 1
    average = "%.2f" % (total / (len(lis) - count_f))
    return average

data_split()
