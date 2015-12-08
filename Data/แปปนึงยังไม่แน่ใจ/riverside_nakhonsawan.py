import csv
def data_split():
    with open('Nakhonsawan.csv', encoding="utf-8") as csvfile:
        test = csv.reader(csvfile)
        list_date = []
        list_do = []
        list_ec = []
        list_temp = []
        for i in test:
            data = i[0].split(';')
            list_date.append(data[2])
            list_do.append(data[4])
            list_ec.append(data[5])
            list_temp.append(data[6])
    list_do = change_value_to_float(list_do)
    list_ec = change_value_to_float(list_ec)
    list_temp = change_value_to_float(list_temp)
    return list_date, list_do, list_ec, list_temp

def change_value_to_float(valu):
    list_value = []
    loop = 0
    for i in valu:
        value = i[1:len(valu[loop])-1]
        if type(value) != str:
            value = float(value)
        list_value.append(value)
        loop += 1
    return list_value

data_split()

##เก็บค่าของแต่ละ value ไว้ในลิสต์ของแต่ละค่า
##ของชัยนาทกับนครสวรรค์นี้มีค่ามากกว่าที่อื่นค่านึง
# ยังไม่ทราบค่า เลยใช้คำว่า unknown value
##สามารแปลงค่าได้ในฟังก์ชั่นเดียว แต่ขี้เกียจแก้แล้ว เลยปล่อยเลยตามเลย
#ถ้าเอาออกก็จะดูสั้นและสวยงามดีมั้ย แต่เราชอบเว่อวัง อิอิ @ณ 00:27 น.
# test del
