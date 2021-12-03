# This is a sample Python script.

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 부산청(101) = [부산항유도등부표(01), 북형제도등대(02), 생도등표(03)]   ex) 부산항유도등부표 = 10101
# 동해청(111) = [묵호항동방파제등대(01), 주문진항동방파제등대(02)]       ex) 묵호항동방파제등대 = 11101
# Data List
list_10101 = []
list_10102 = []
list_10103 = []
list_11101 = []
list_11102 = []
# Header List
header_10101 = []
header_10102 = []
header_10103 = []
header_11101 = []
header_11102 = []

list_months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def readCSV():
    file_status = 'status.csv'
    file_weather = 'weather.csv'

    temp = []
    header = []

    first_loop_10101 = True
    first_loop_10102 = True
    first_loop_10103 = True
    first_loop_11101 = True
    first_loop_11102 = True
    with open(file_status, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if '지방청' in row[0]:
                header = row

            elif '부산항' in row[1]:
                count = 4
                for val in row[4:]:
                    if len(val) > 0:
                        temp.append(float(val))
                        if first_loop_10101: #헤더 추출
                            header_10101.append(header[count])
                    count += 1
                first_loop_10101 = False
                list_10101.append(temp)
                temp = []

            elif '북형제' in row[1]:
                count = 4
                for val in row[4:]:
                    if len(val) > 0:
                        temp.append(float(val))
                        if first_loop_10102:  # 헤더 추출
                            header_10102.append(header[count])
                    count += 1
                first_loop_10102 = False
                list_10102.append(temp)
                temp = []

            elif '생도등' in row[1]:
                count = 4
                for val in row[4:]:
                    if len(val) > 0:
                        temp.append(float(val))
                        if first_loop_10103:  # 헤더 추출
                            header_10103.append(header[count])
                    count += 1
                first_loop_10103 = False
                list_10103.append(temp)
                temp = []

            elif '묵호항' in row[1]:
                count = 4
                for val in row[4:]:
                    if len(val) > 0:
                        temp.append(float(val))
                        if first_loop_11101:  # 헤더 추출
                            header_11101.append(header[count])
                    count += 1
                first_loop_11101 = False
                list_11101.append(temp)
                temp = []

            elif '주문진' in row[1]:
                count = 4
                for val in row[4:]:
                    if len(val) > 0:
                        temp.append(float(val))
                        if first_loop_11102:  # 헤더 추출
                            header_11102.append(header[count])
                    count += 1
                first_loop_11102 = False
                list_11102.append(temp)
                temp = []

def divideFile(list, header, file_name):
    with open(file_name, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(list)


def sortList(list):
    # 오름차순
    list.sort(key=lambda x: x[0])

    # 내림차순
    #list.sort(key=lambda x: -x[0])

def makePlot(lighthouse_name, list, header_list, header_str, date_input):
    endpoint = False
    x = []
    y = []
    x_label = []
    index = header_list.index(header_str)
    print('Parameter : ', header_str)
    print('Header index : ', index)
    print('Data : ', len(list))
    plt.figure()
    ax = plt.subplot()
    title = ''
    for raw in list:
        date = timeFormat(raw)
        if str(date.date()) == date_input:
            hms = date.time()
            ymd = str(date.year) + "/" + str(date.month) + "/" + str(date.day)
            title = lighthouse_name + header_str + "(" + str(ymd) + ")"
            x.append(str(hms))
            y.append(raw[index])
            endpoint = True

        elif str(date.date()) != date_input:
            if endpoint is True:
                plt.title(title)
                plt.plot(x, y)
                ax.xaxis.set_major_locator(plt.MultipleLocator(10))
                plt.xticks(rotation=45, fontsize='small', ha='right')

                break
    plt.show()

def timeFormat(list):
    date = str(list[0])
    date = datetime(year=int(date[0:4]), month=int(date[4:6]), day=int(date[6:8]), hour=int(date[8:10]),
                    minute=int(date[10:12]), second=int(date[12:14]))
    # print(date.hour, ":", date.minute, ":", date.second)
    return date

if __name__ == '__main__':
    readCSV()

    list_name = input('등대 입력 : ')

    if '부산항' in list_name:
        lighthouse_name = '[BUSAN] '
        list = list_10101
        header_list = header_10101

    elif '북형제' in list_name:
        lighthouse_name = '[BUKHY] '
        list = list_10102
        header_list = header_10102

    elif '생도등' in list_name:
        lighthouse_name = '[SANGDO] '
        list = list_10103
        header_list = header_10103

    elif '묵호항' in list_name:
        lighthouse_name = '[MUKHO] '
        list = list_11101
        header_list = header_11101

    elif '주문진' in list_name:
        lighthouse_name = '[JUMUNJIN] '
        list = list_11102
        header_list = header_11102

    print('Header list : ', header_list)
    header_str = input('파라미터 입력 : ')
    date_input = input('날짜 입력(ex. 2021-01-01) : ')

    #------------------Debug----------------------
    # lighthouse_name = '[BUSAN] '
    # list = list_10101
    # list_name = list_10101
    # header_list = header_10101
    # header_str = 'MAIN_VOLT_STATUS'
    # date_input = '2021-02-23'
    #----------------------------------------------

    sortList(list)
    makePlot(lighthouse_name, list, header_list, header_str, date_input)

    # Divide data
    # file_name = 'status_sdd.csv'
    # divineFile(list_10103, header_10103, file_name)