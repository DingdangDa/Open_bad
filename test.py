# 一些测试用的语句。一般用不上

# 申请场公告
res = requests.post(url='http://wechat.njust.edu.cn/api/v2/appGym/getUserBookConfigInfo',
                    headers={"Connection": "keep-alive",
                              "Content-Length": "85",
                              "Accept": "application/json, text/plain, */*",
                              "User-Agent": "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20220604 Mobile Safari/537.36 MMWEBID/9055 MicroMessenger/8.0.24.2180(0x28001853) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
                              "Content-Type": "application/json",
                              "Origin": "http://wechat.njust.edu.cn",
                              "X-Requested-With": "com.tencent.mm",
                              "Referer": "http://wechat.njust.edu.cn/gymBooking/venueBooking.html",
                              "Accept-Encoding": "gzip, deflate",
                              "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                              "Cookie": 
                             },
                    json={"id":"790c8055a06311e8a69022faa7560813","siteId":"4007243990b243938283ce51ea5af072"})
print(res.text)

# 申请场
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
                                 "Cookie": 
                                 },
                        json={"siteId": "e1f5c85e86c34c46a2d0935452094b77", "bookDate": tomorrowDate})
print(res.text)

# 订场
res = requests.post(url='http://wechat.njust.edu.cn/api/v2/appGym/submitAreaOrder',
                        headers={"Connection": "keep-alive",
                                 "Content-Length": "396",
                                 "Accept": "application/json, text/plain, */*",
                                 "User-Agent": "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20220604 Mobile Safari/537.36 MMWEBID/9055 MicroMessenger/8.0.24.2180(0x28001853) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
                                 "Content-Type": "application/json",
                                 "Origin": "http://wechat.njust.edu.cn",
                                 "X-Requested-With": "com.tencent.mm",
                                 "Referer": "http://wechat.njust.edu.cn/gymBooking/venueBooking.html",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Cookie": 
                                 },
                        json={"siteId": "4007243990b243938283ce51ea5af072",
                              "gymId": "790c8055a06311e8a69022faa7560813",
                              "payAmount": 5, "payDuration": 60,
                              "areaRecordList": [{"areaId": "cd7a72e4c5a24938b7f3c8db66f79964",
                                                  "areaName": "1",
                                                  "bookingType": "",
                                                  "bookingDate": "2022-11-18",
                                                  "timeId": "204e318d4f634a0c921a354a16280107",
                                                  "time": "18:00~19:00",
                                                  "userType": 1,
                                                  "price": 5,
                                                  "areaPriceId": "6e769af51679429594dbdfaedb94595b"}],
                              "bookTimes": 1}
                        )
    print(res.text)


headers={"Connection": "keep-alive",
                                 "Content-Length": "396",
                                 "Accept": "application/json, text/plain, */*",
                                 "User-Agent": "Mozilla/5.0 (Linux; Android 12; XQ-AT72 Build/58.2.A.10.44; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4343 MMWEBSDK/20220604 Mobile Safari/537.36 MMWEBID/9055 MicroMessenger/8.0.24.2180(0x28001853) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
                                 "Content-Type": "application/json",
                                 "Origin": "http://wechat.njust.edu.cn",
                                 "X-Requested-With": "com.tencent.mm",
                                 "Referer": "http://wechat.njust.edu.cn/gymBooking/venueBooking.html",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Cookie": 
                                 },
