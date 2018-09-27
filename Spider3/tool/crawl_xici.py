import scrapy
import requests
from scrapy.selector import Selector
import MySQLdb

# 连接数据库
conn = MySQLdb.connect(host="127.0.0.1",user="ding",password ="",
                       db = "test",charset= 'utf8',use_unicode=True)
cursor = conn.cursor()
def crawl_ip():
     # 设置头部信息
     header ={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
     # 进行循环匹配每个页面信息
     for i in range(3369):
         # 访问网页
         ret = requests.get('http://www.xicidaili.com/nn/'+str(i),headers = header)
         res = Selector(text = ret.text)
         ip = res.xpath("//tr[@class='odd']/td[2]/text()").extract()
         port = res.xpath("//tr[@class='odd']/td[3]/text()").extract()
         http_type = res.xpath("//tr[@class='odd']/td[6]/text()").extract()
         speed = res.xpath("//div[@class='bar']/@title").extract()
         print(ip)
crawl_ip()

#          all_trs = res.css("#ip_list tr")
#          ip_list = []
#          for tr in all_trs[1:]:
#             all_text = tr.css('td::text').extract()
#             ip = all_text[0]
#             port = all_text[1]
#             proxy_type = all_text[5]
#             speed = tr.css(".bar::attr(title)").extract()[0]
#             speed = float(speed.split('秒')[0])
#             ip_list.append((ip, port, proxy_type, speed))
#
#          for ip_info in ip_list:
#                 cursor.execute(""" insert into proxy_ip(ip,port,proxy_type,speed)
#                 VALUES("{3}","{1}","{2}","{0}")""".format(ip_info[0],ip_info[1],ip_info[2],ip_info[3]))
#                 conn.commit()
#
# class GetIP(object):
#     #从数据库中删除ip
#     def delete_ip(self,ip):
#         delete_ip ="""
#         delete from proxy_ip where ip='{0}'
#         """.format(ip)
#         cursor.execute(delete_ip)
#         cursor.commit()
#         return True
#
#
#
#     #判断ip是否可用
#     def judge_ip(self,ip,port,proxy):
#         http_url = "http://httpbin.org/get"
#         proxy_url = "http://{0}:{1}".format(ip,port)
#         try:
#             proxy_dict = {
#                 "{}".format(proxy): proxy_url
#             }
#             print(proxy_dict)
#             response = requests.get(http_url, proxies=proxy_dict,timeout=10)
#             print(response.content)
#         except Exception as e :
#             print('invalid ip and port')
#             self.delete_ip(ip)
#             return False
#         else:
#             code = response.status_code
#             if code >=200 and code < 300:
#                print("effective ip", code)
#                return True
#             else:
#                print("invalid ip and port")
#                self.delete_ip(ip)
#                return False




    # #从数据库中随机取出一个ip
    # def get_random_ip(self):
    #     random_sql = """
    #     SELECT ip, port,proxy_type FROM proxy_ip
    #     ORDER BY RAND()
    #     LIMIT 1
    #     """
    #     result = cursor.execute(random_sql)
    #     for ip_info in cursor.fetchall():
    #         ip = ip_info[0]
    #         port = ip_info[1]
    #         proxy = ip_info[2]
    #         judge_re = self.judge_ip(ip,port,proxy)
    #         if judge_re:
    #              return  "http://{0}:{1}".format(ip,port)
    #         else:
    #              return self.get_random_ip()

# if __name__ == "__main__":
#         get_ip = GetIP()
#         get_ip.get_random_ip()