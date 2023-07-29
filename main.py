import pandas as pd
import numpy as np

order_list = pd.read_csv('orders_table.csv', encoding = 'CP949', usecols = [0,3,4,5,6,8,9,10])
#print(order_list)

# '하차가능시간_시작' 열에서 숫자 부분을 추출하는 사용자 정의 함수
def convert_to_time(s):
    time_format = '%H:%M'
    return pd.to_datetime(s, format=time_format, errors='coerce').dt.strftime('%H:%M')

order_list['하차가능시간_시작'] = convert_to_time(order_list['하차가능시간_시작'])

order_list_by_date_Group = order_list.sort_values(by=['date', 'Group', '터미널ID', '하차가능시간_시작'])
print(order_list_by_date_Group)
