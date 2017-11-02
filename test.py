import requests
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx?ID=SCPD&subBase=all',
'Cookie': 'cnkiUserKey=e01110a4-d552-48f6-32b5-999450e9ff06;Ecp_ClientId=2170909081801313483;kc_cnki_net_uid=76e702f3-b239-278d-1fd7-05d3143f2c9c;Ecp_IpLoginFail=170929112.81.2.110;ASP.NET_SessionId=ht0penalaziomf55bodfyt55;AutoIpLogin=; LID=;c_m_LinID=LinID=WEEvREcwSlJHSldRa1Fhb09jMjQyNUcrUUV5bWtMMllPL0g1YzNRN29VND0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=09/29/2017 17:30:50;c_m_expire=2017-09-29 17:30:50; SID=130101;FileNameM=cnki%3A'
}
i =2
data = {
'curpage':i,
'RecordsPerPage':'50',
'QueryID':'4',
'ID':'SCPD',
'turnpage':'1'
}
proxies = {

}
url ='http://dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx'
r = requests.post(url=url,params=data,headers=headers,proxies=proxies)
print(r.text)
print(r.url)