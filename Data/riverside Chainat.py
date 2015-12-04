import csv
def project_um():
    with open('Chainat.csv', encoding="utf-8") as csvfile:
        test = csv.reader(csvfile)
        date = []
        unknown_val = []
        value1 = []
        value2 = []
        value3 = []
        value4 = []
        value5 = []
        for i in test:
            data = i[0].split(';')
            date.append(data[2])
            unknown_val.append(data[3])
            value1.append(data[4])
            value2.append(data[5])
            value3.append(data[6])
            value4.append(data[7])
            value5.append(data[8])
    lst_val_un = change_value_to_float(unknown_val)
    lst_val_1 = change_value_to_float(value1)
    lst_val_2 = change_value_to_float(value2)
    lst_val_3 = change_value_to_float(value3)
    lst_val_4 = change_value_to_string(value4)
    lst_val_5 = change_value_to_string(value5)

    return lst_val_un, lst_val_1, lst_val_2, lst_val_3, lst_val_4, lst_val_5

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

def change_value_to_string(valu):
    list_value = []
    loop = 0
    for i in valu:
        value = i[1:len(valu[loop])-1]
        list_value.append(value)
        loop += 1
    return(list_value)
    
print(project_um())

##เก็บค่าของแต่ละ value ไว้ในลิสต์ของแต่ละค่า
##ของชัยนาทกับนครสวรรค์นี้มีค่ามากกว่าที่อื่นค่านึง
# ยังไม่ทราบค่า เลยใช้คำว่า unknown value
##สามารแปลงค่าได้ในฟังก์ชั่นเดียว แต่ขี้เกียจแก้แล้ว เลยปล่อยเลยตามเลย
#ถ้าเอาออกก็จะดูสั้นและสวยงามดีมั้ย แต่เราชอบเว่อวัง อิอิ @ณ 00:27 น.
