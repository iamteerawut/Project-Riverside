import csv
def project_um():
    with open('Bangsai.csv', encoding="utf-8") as csvfile:
        test = csv.reader(csvfile)
        date = []
        value1 = []
        value2 = []
        value3 = []
        value4 = []
        value5 = []
        for i in test:
            data = i[0].split(";")
            date.append(data[1])
            value1.append(data[2])
            value2.append(data[3])
            value3.append(data[4])
            value4.append(data[5])
            value5.append(data[6])
    lst_val_1 = change_value_to_float(value1)
    lst_val_2 = change_value_to_float(value2)
    lst_val_3 = change_value_to_float(value3)
    lst_val_4 = change_value_to_string(value4)
    lst_val_5 = change_value_to_string(value5)

    return lst_val_1[0], lst_val_2[0], lst_val_3[0], lst_val_4[0], lst_val_5[0]

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

def change_value_to_string(valu):
    list_value = []
    loop = 0
    for i in valu:
        value = i[1:len(valu[loop])-1]
        list_value.append(value)
        loop += 1
    return(list_value)
    
print(project_um())
