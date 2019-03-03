#coding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import hashlib
import sys


sys.path.append('/home/test/python/test/class')#加载类文件夹
from mainclass import allMethod #引用类及其方法

'''
dt=datetime.now()
dt=dt.strftime('%Y-%m-%d')
'''

        
def getData():
    #get url
    res_tmp= requests.get("http://www.qdnhb.gov.cn/hjjc/kqzl.htm")
    res_tmp.encoding='utf-8'
    soup_tmp=BeautifulSoup(res_tmp.text,'lxml')
    url_tmp=soup_tmp.find_all('a',class_='c12176')[0]
    url_tmp=url_tmp.get('href').replace('..','http://www.qdnhb.gov.cn')

    #get table
    res = requests.get(url_tmp)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'lxml')
    tables = soup.find_all('table')

    #get title
    dt=soup.find_all('td',class_='titlestyle12124')[0].text.replace(' ','').replace('\r\n','')[0:10]
    md5 = hashlib.md5()
    md5.update(dt.encode('utf-8'))
    flag=md5.hexdigest()

    #to dataframe
    df = pd.read_html(str(tables[12])) #list
    df=pd.concat(df)#dataframe
    df.columns=['县市','空气质量指数','空气等级','空气质量状况']
    df =df.drop([0,1],axis = 0,inplace = False)

    #reset index from 0
    df=df.reset_index(drop=True)

    #add new colunms
    df.insert(0,'日期',dt)
    df.insert(0,'flag',flag)
    return df,flag


#save to csv
msg=''

if os.path.exists('黔东南州空气质量.csv')==True:
    old_df=pd.read_csv('黔东南州空气质量.csv',encoding='utf-8_sig')
    if len(old_df[(old_df.flag==getData()[1])].index.tolist())==0: #判断日期是否是今天
        df=getData()[0] #调用爬取函数
        df.to_csv('黔东南州空气质量.csv',encoding='utf-8_sig',mode='a',header=False)#追加
        msg=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 爬取成功！'
    else:
        msg='<font color=red>'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 目标网站无更新，放弃爬取！</font>'
else:
    df=getData()[0]
    df.to_csv('黔东南州空气质量.csv',encoding='utf-8_sig')#创建并写入
    msg=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' 创建日志，爬取成功！'

if __name__ == "__main__":
    x=allMethod("<font color=red>"+msg+":<br><img src=\"cid:weekly\" border=\"0\"><br>详细内容见附件。</font>")#注意插入图片的写法，是基于html的
    x.WriteTo()
    x.mailto()