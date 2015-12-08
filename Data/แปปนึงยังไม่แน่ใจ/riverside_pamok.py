import csv
def data_split():
    with open('Pamok.csv') as csvfile:
        test = csv.reader(csvfile)
        list_date = []
        list_do = []
        list_ec = []
        list_temp = []
        for i in test:
            list_date.append(i[1])
            list_do.append(i[2])
            list_ec.append(i[3])
            list_temp.append(i[4])
    list_do = change_value_to_float(list_do)
    list_ec = change_value_to_float(list_ec)
    list_temp = change_value_to_float(list_temp)
    return list_date, list_do, list_ec, list_temp

def change_value_to_float(data):
    list_data = []
    for i in range(1, len(data)):
        if data[i] != 'F':
            data[i] = float(data[i])
        list_data.append(data[i])
    return list_data

data_split()
#อ้าว จ๋าแก้แล้วนิหว่า = =''
#do = ปริมาณออกซิเจนที่ละลายในน้ำ ค่าเป็นเลขหลักเดียวกับทศนิยม เช่น 5.8, 6.4
#ec = ค่าความนำไฟฟ้า ค่าส่วนใหญ่เป็นเลขสามหลักกับทศนิยม เช่น 148.3, 154.5
#temp = อุณภูมิน้ำ ค่าส่วนใหญ่เป็นเลขสองหลักกับทศนิยม เช่น 19.5, 33.0
#อย่างที่ฟลุ๊คบอกตอนไหนสักตอนป่าโมกมันเกลียด utf-8 เลยเอาออก งงชื่อตัวแปลจ๋าเอาใส่แล้วมันเอ๋อก็เลยเขียนใหม่ -.,-
