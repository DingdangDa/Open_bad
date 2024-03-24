#！/usr/bin/env python3
import requests
import time
import data
import threading
import json
from datetime import date, timedelta

# 乒乓球siteId 4007243990b243938283ce51ea5af072
# 羽毛球siteId e1f5c85e86c34c46a2d0935452094b77

def post_newsType():
    res = requests.post(url='http://wechat.njust.edu.cn/api/v2/appGymMicroportal/newsType/search',
                        headers={"Connection": "keep-alive",
                                 "Content-Length": "2",
                                 "Accept": "application/json, text/plain, */*",
                                 "User-Agent": "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/9055 MicroMessenger/8.0.47.2560(0x28002F50) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
                                 "Content-Type": "application/json",
                                 "X-Requested-With": "com.tencent.mm",
                                 "Referer": "http://wechat.njust.edu.cn/wechat/gymMicroportal/gymMicroportal.html",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Cookie": Cookie
                                 },
                        json={})

def ask_bad():  # 申请场信息
    global localtime
    ask_time = time.strftime("%m-%d %H:%M:%S")
    print(ask_time, "thread_ask_bad.start")
    res = requests.post(url='http://wechat.njust.edu.cn/api/v2/appGym/listAreaPriceBySiteIdAndTime',
                        headers={"Connection": "keep-alive",
                                 "Content-Length": "69",
                                 "Accept": "application/json, text/plain, */*",
                                 "User-Agent": "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20220604 Mobile Safari/537.36 MMWEBID/9055 MicroMessenger/8.0.24.2180(0x28001853) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
                                 "Content-Type": "application/json",
                                 "Origin": "http://wechat.njust.edu.cn",
                                 "X-Requested-With": "com.tencent.mm",
                                 "Referer": "http://wechat.njust.edu.cn/gymBooking/venueBooking.html",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Cookie": "JSESSIONID=5FF4895930462F485775D74EB2588411; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvdCI6IndlY2hhdF9xeSIsInR0IjoiZGF0YWJhc2UiLCJvIjoiOTIwMTA0MEcxMjIzIiwibm93IjoxNjgzNjQ1Njc2LCJleHAiOjE2ODM2NDkyNzYsInQiOiI5MjAxMDQwRzEyMjMifQ.PY4Sv1V7bOUohHu-DNMAURxZBceDCkSoSMMorbzma5g"
                                 },
                        json={"siteId": "e1f5c85e86c34c46a2d0935452094b77", "bookDate": tomorrowDate})
    print(res.text)
    data.areaBack = res.text  # data.areaBack这是一个全局变量，会在while1中被用
    log_write(99, 99, res.text, "ask", "HXY")
    if res.text.endswith('null}', 0, len(res.text)) == 1:
        print(time.strftime("%m-%d %H:%M:%S"), "thread_ask_bad.get ask time:", ask_time)

def book_bad(BookTime, BookArea, PersonName, PersonCode, PersonAgent, ContentLength, BookPersonNum):  # 订场
    # print(BookTime, BookArea)
    if BookTime == 0:
        timeSend = "0" + str(BookTime + 8) + ":00-0" + str(BookTime + 9) + ":00"
    elif BookTime == 1:
        timeSend = "0" + str(BookTime + 8) + ":00-" + str(BookTime + 9) + ":00"
    else:
        timeSend = str(BookTime + 8) + ":00-" + str(BookTime + 9) + ":00"
    BookSendTime = time.strftime("%m-%d %H:%M:%S")
    res = requests.post(url='http://wechat.njust.edu.cn/api/v2/appGym/submitAreaOrder',
                        headers={"Connection": "keep-alive",
                                 "Content-Length": ContentLength,
                                 "Accept": "application/json, text/plain, */*",
                                 "User-Agent": PersonAgent,
                                 "Content-Type": "application/json",
                                 "Origin": "http://wechat.njust.edu.cn",
                                 "X-Requested-With": "com.tencent.mm",
                                 "Referer": "http://wechat.njust.edu.cn/gymBooking/venueBooking.html",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Cookie": PersonCode
                                 },
                        json={"siteId": "e1f5c85e86c34c46a2d0935452094b77",
                              "gymId": "790c8055a06311e8a69022faa7560813",
                              "payAmount": data_dic['data'][BookTime]['listAreaPrice'][BookArea]['price'], "payDuration": 60,
                              "areaRecordList": [{"areaId": data_dic['data'][BookTime]['listAreaPrice'][BookArea]['areaId'],
                                                  "areaName": data_dic['data'][BookTime]['listAreaPrice'][BookArea]['areaName'],
                                                  "bookingType": "",
                                                  "bookingDate": tomorrowDate,
                                                  "timeId": data_dic['data'][BookTime]['listAreaPrice'][BookArea]['timeId'],
                                                  "time": timeSend,
                                                  "userType": 1,
                                                  "price": data_dic['data'][BookTime]['listAreaPrice'][BookArea]['price'],
                                                  "areaPriceId": data_dic['data'][BookTime]['listAreaPrice'][BookArea]['areaPriceId'],
                                                  }],
                              "bookTimes": 1}
                        )
    log_write(BookTime, BookArea, res.text, "book", PersonName)  # def log_write(BookTime, BookArea, ResText, Type, Name)
    book_print(BookTime, BookArea, res.text, PersonName, BookSendTime, BookPersonNum)


def book_bad_ctrl(BookTime, BookArea, Number):  # 订场线程，用于调用订场函数，存在这样一个中间商是方便调试的时候注释
    match Number:
        case 1:
            PersonName = "H"
            PersonCode = "JSESSIONID=B103E07F296DEE37C8935FA17D6C0E3F; lxwxuserid=7dJc9a/SoSSWSlamAY1PaQ=="  # old code
            PersonCode = "JSESSIONID=12F21326B05A6E67DB9AFBE7B7C9B42D; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0IjoiOTIwMTA0MEcxMjIzIiwib3QiOiJ3ZWNoYXRfcXkiLCJ0dCI6ImRhdGFiYXNlIiwibyI6IjkyMDEwNDBHMTIyMyIsIm5vdyI6MTY4MzE1ODc2MywiZXhwIjoxNjgzMTYyMzYzfQ.yzsChrbFTavzz2dUg7eZ9fawtLIPNZEtKPIQtWGREJo"
            PersonAgent = "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20220604 Mobile Safari/537.36 MMWEBID/9055 MicroMessenger/8.0.24.2180(0x28001853) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64"
            ContentLength = "396"
            book_bad(BookTime, BookArea, PersonName, PersonCode, PersonAgent, ContentLength, Number)
        case 2:
            PersonName = "L"
            PersonCode = "JSESSIONID=743055D21CD36D6D45AB19D62621D550; lxwxuserid=qEbDEi/9jloAiDu2ohD2eA=="
            PersonAgent = "Mozilla/5.0 (Linux; Android 10; ELS-AN00 Build/HUAWEIELS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4365 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9420 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"
            ContentLength = "368"
            book_bad(BookTime, BookArea, PersonName, PersonCode, PersonAgent, ContentLength, Number)
        case 3:
            PersonName = "Z"
            PersonCode = "JSESSIONID=FEF0BCA74ED514A5150412170F839519; lxwxuserid=lOSjkvvY4Pr+fUGfWbsfnA=="
            PersonAgent = "Mozilla/5.0 (Linux; Android 12; ELS-AN00 Build/HUAWEIELS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5015 MMWEBSDK/20221206 MMWEBID/2952 MicroMessenger/8.0.32.2300(0x2800205D) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64"
            ContentLength = "368"
            book_bad(BookTime, BookArea, PersonName, PersonCode, PersonAgent, ContentLength, Number)

def log_write(BookTime, BookArea, ResText, Type, Name):
    txtName = "./" + time.strftime("%Y-%m-%d ") + Name + " " + Type + "_log.txt"  # ./2022-12-13 L book_log.txt
    log = open(txtName, "a", encoding="UTF-8")
    log.write(time.strftime("%m-%d %H:%M:%S"))
    log.write(Name)
    log.write(Type)
    log.write(": ")
    if BookTime != 99 and BookArea != 99:
        log.write(str(BookTime * 100 + BookArea))
    log.write(ResText)
    log.write("\n")
    log.close()  # 关闭打开的文件


def book_print(BookTime, BookArea, BookRes, BookerName, BookSendTime, BookPersonNum):
    if BookRes.find("success", 0, len(BookRes)) != -1:  # 成功订到了
        BookSuccessList.append(BookPersonNum * 10000 + BookTime * 100 + BookArea)
        BadBookTimeList.remove(BookTime)  # 从列表移除
        print(time.strftime("%m-%d %H:%M:%S"), "Booked:", BookerName, BookTime * 100 + BookArea, "success 订到了", "send time:", BookSendTime)
    elif BookRes.find("-1", 0, len(BookRes)) != -1:  # 没有订到
        print(time.strftime("%m-%d %H:%M:%S"), "Booked:", BookerName, BookTime * 100 + BookArea, "G:-1 没有订到", "send time:", BookSendTime)
    elif BookRes.find("503", 0, len(BookRes)) != -1:
        print(time.strftime("%m-%d %H:%M:%S"), "Booked:", BookerName, BookTime * 100 + BookArea, "G:503", "send time:", BookSendTime)
    else:
        print(time.strftime("%m-%d %H:%M:%S"), "Booked:", BookerName, BookTime * 100 + BookArea, "Unknown G", "send time:", BookSendTime)


def ask_ctrl():
    global ask_ctrl_thread_start
    global localtime
    while 1:
        ask = threading.Thread(target=ask_bad)
        ask.start()
        time.sleep(0.5)
        if localtime[3] == 8 and localtime[4] == 1:  # 早上8:01，这会结束这个线程
            ask_ctrl_thread_start = 1
            break


def time_get():  # 更新时间
    global localtime
    while 1:
        localtime = time.localtime(time.time())
        time.sleep(0.1)


def tomorrow_date():  # 计算明天的日期
    global tomorrowDate
    global tomorrowDay
    tomorrowDate = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    print("Tomorrow Date:", tomorrowDate)
    tomorrowDay = 7 if int((date.today() + timedelta(days=1)).strftime("%w")) == 0 else int((date.today() + timedelta(days=1)).strftime("%w"))  # date.today的周日是0
    print("tomorrow Day:", tomorrowDay)


def book_time_list():
    global BadBookTimeList
    if tomorrowDay == 6 or tomorrowDay == 7:  # 明天周六或周日
        BadBookTimeList = [3, 2, 1, 0]  # 早上4场
    elif tomorrowDay == 3:  # 明天周三
        BadBookTimeList = [6, 7, 8, 12, 11, 13, 10]  # 下午14-17三场，晚上4场
    else:  # 明天周一、周二、周四、周五 tomorrowDay == 1，2，4，5
        BadBookTimeList = [12, 11, 13, 10]  # 晚上4场
    print("Goat book time:", end=" ")
    for i in range(len(BadBookTimeList)):
        print(BadBookTimeList[i] + 8, "-", BadBookTimeList[i] + 9, end=" ")
    print(" ")


# 从这开始执行
localtime = time.localtime(time.time())  # 获取一次时间
print("Today:", localtime[0], "-", localtime[1], "-", localtime[2], ",", localtime[3], ":", localtime[4], ":", localtime[5], ", 周", localtime[6] + 1)

tomorrowDate = ""  # 声明tomorrowDate，是明天的年-月-日
tomorrowDay = 2  # 声明tomorrowDay，是明天周几
tomorrow_date()  # 计算一下明天的日期

# 声明成功订到的场次
BookSuccessList = []

# 获取系统时间的线程，创建与开始
thread_time = threading.Thread(target=time_get)
thread_time.start()

# 声明BadBookTimeList，储存要定什么时候的场
BadBookTimeList = []
# 根据明天的周几计算要定哪些场，好生成线程
book_time_list()

ask_ctrl_thread_start = 0  # 标记是否开启了线程ask_ctrl_thread

BookJustNow = 0  # 标记循环里是不是订了场
BookNum = 1

Cookie = ""
# Cookie: TGC=TGT-8f357dfadf3f4b5f9708a7b8ea85ae78; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJub3ciOjE3MTEyNTYyMjgsIm90Ijoid2VjaGF0X3F5IiwidHQiOiJkYXRhYmFzZSIsInQiOiI5MjAxMDQwRzEyMjMiLCJleHAiOjE3MTEyNTk4MjgsIm8iOiI5MjAxMDQwRzEyMjMifQ.uGoHFvOabqG0qbIHSWU1qOgW9OHdKkwJLsDoltb4c5I


res = requests.get(url='http://wechat.njust.edu.cn/gymMicroportal/gymMicroportal.html?i=1',
                        headers={"Connection": "keep-alive",
                                 "Upgrade-Insecure-Requests": "1",
                                 "User-Agent": "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5061 MMWEBSDK/20220604 MMWEBID/9055 MicroMessenger/8.0.24.2180(0x28001853) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                                 "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                 "X-Requested-With": "com.tencent.mm",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvIjoiOTIwMTA0MEcxMjIzIiwidHQiOiJ3ZWNoYXRfcXkiLCJleHAiOjE2ODM4MzA4NzAsIm90Ijoid2VjaGF0X3F5IiwidCI6IjkyMDEwNDBHMTIyMyIsIm5vdyI6MTY4MzgyNzI3MH0.KUEaEYBtddCZc8IOeA33VgxNplVgsiAxYzB0Iujl0yY                                                                                                               "
                                 },)
print(res.headers)
print(res.text)
headers = str(res.headers)
print("111")
print(headers)
print(headers.endswith('}', 0, len(headers)))
headers.lstrip()
headers.rstrip()
#headers = headers.lstrip("{")
#headers = headers.rstrip("}")
print(headers)
headers_dic = eval(headers)
print(headers_dic['Set-Cookie'])

while 1:
    if localtime[3] == 7 and 59 <= localtime[4]:  # 早上7:59
        post_newsType()

    if localtime[3] == 8 and 0 <= localtime[4] <= 2:  # 早上8:00-8:02
    # if 1:

        # 创建与开始申请场信息的线程（在8:00）
        if ask_ctrl_thread_start == 0:  # 单独开一个线程，来开ask线程，为了及时更新场信息
            ask_ctrl_thread = threading.Thread(target=ask_ctrl)
            ask_ctrl_thread.start()
            ask_ctrl_thread_start = 1

        if data.areaBack.endswith('t": 0}]}', 0, len(data.areaBack)) == 1:  # 如果获取到了场信息
            data_dic = json.loads(data.areaBack)  # 解析返回数据json

            # 订场
            for BadBookTime in BadBookTimeList:  # 在要抢的时间范围内
                for BadBookArea in range(1, 17):
                    if data_dic['data'][BadBookTime]['listAreaPrice'][BadBookArea]['status'] == 0:  # 如果没有被订
                        Book = threading.Thread(target=book_bad_ctrl, args=(BadBookTime, BadBookArea, BookNum,))
                        Book.start()
                        if BookNum == 3:
                            BookNum = 1
                        else:
                            BookNum = BookNum + 1

                        time.sleep(0.3)  # 避免太猛，缓一下
                        BookJustNow = 1

                        break  # 跳出去，去订下一个时间段，避免盯着一个时间段订

            for BookSuccess in BookSuccessList:
                print("Person", int(BookSuccess / 10000), "订到了", int(BookSuccess / 100 - BookSuccess / 10000 * 100 + 8), "点开始", BookSuccess - int(BookSuccess / 10000) * 10000 + 1, "号场")

            if BookJustNow == 0:  # 刚刚没订
                time.sleep(0.8)
            else:  # 刚刚订了
                BookJustNow = 0

            if len(BadBookTimeList) == 0:  # 订到了要的所有时间的场的话，再刷新一遍目标场时间，继续订
                book_time_list()

    elif localtime[3] == 8 and localtime[4] == 5 and localtime[5] == 0:  # 早上8:05:00。报告抢到了什么
        print("8:05")
        for BookSuccess in BookSuccessList:
            print("Person", int(BookSuccess / 10000), "订到了", int(BookSuccess / 100 - BookSuccess / 10000 * 100 + 8), "点开始", BookSuccess - int(BookSuccess / 10000) * 10000 + 1, "号场")
        ask_ctrl_thread_start = 0
        time.sleep(0.5)

    elif localtime[3] == 7 and localtime[4] == 59:  # 早上7:59，为抢场地做准备
        print("Now:", localtime[0], "-", localtime[1], "-", localtime[2], ",", localtime[3], ":", localtime[4], ":", localtime[5], ", 周", localtime[6] + 1)
        tomorrow_date()  # 计算一下明天的日期
        book_time_list()  # 根据明天的周几计算要定哪些场，好生成线程
        BookSuccessList = []
        time.sleep(0.5)

    else:
        time.sleep(30)  # 不在需要工作的时间

# pyinstaller --console --onefile main.py
# pyinstaller -F main.py --hidden-import requests
