import get_ticket 
import json
import requests
import prettytable as pt

f = open('city.json',encoding='utf=8')
txt = f.read()
json_data = json.loads(txt)
from_station = input('请输入你出发的城市：')
to_station = input('请输入你到达的城市：')
date = input('请输入你要出发的日期(格式:2022-05-04)')

url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_station]}&leftTicketDTO.to_station={json_data[to_station]}&purpose_codes=ADULT'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie':'_uab_collina=170364542312604648830089; JSESSIONID=896F05F94E837D10B9B60A9A9E975628; _jc_save_toDate=2023-12-27; _jc_save_wfdc_flag=dc; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u5317%u4EAC%2CBJP; BIGipServerpassport=887619850.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1911030026.50210.0000; _jc_save_toStation=%u6210%u90FD%2CCDW; _jc_save_fromDate=2023-12-30'
                         }
response = requests.get(url,headers=headers)
tb = pt.PrettyTable()
tb.field_names = [
        '序号',
        '车次',
        '出发时间',
        '到达时间',
        '耗时',
        '特等座',
        '一等',
        '二等',
        '软卧',
        '硬卧',
        '硬座',
        '无座',
]
page = 1
for index in response.json()['data']['result']:
    info = index.split('|')
    num = info[3]
    start_time = info[8]
    end_time = info[9]
    use_time = info[10]
    topGrade = info[32] # 特等座
    first_class = info[31] # 一等
    second_class = info[30]#二等
    soft_sleeper = info[23] # 软
    hard_sleeper = info[28] # 便
    hard_seat = info [29]
    no_seat = info[26]# 无座
    
    tb.add_row([
        page,
        num,
        start_time,
        end_time,
        use_time,
        topGrade,
        first_class,
        second_class,
        soft_sleeper,
        hard_sleeper,
        hard_seat,
        no_seat,
    ])
    page += 1
print(tb)
word = input('请输入你想要购买的车票:')
get_ticket.get_ticket(int(word),from_station,to_station,date)