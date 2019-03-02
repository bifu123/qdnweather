#!/usr/bin/python
# -*- coding: UTF-8 -*-
class allMethod(object):
    """docstring for ClassName"""
    def __init__(self, msg):
        self.msg=msg
        
    def WriteTo(self):
        import os
        fi=open('log.txt',mode='a')
        fi.write('%s'%(self.msg))
        fi.write('\n')
        fi.close()
        os.system('sudo chmod 777 log.txt')

    #x=WriteToLog().WriteTo('dog')

    def mailto(self):
        import smtplib
        from email.mime.text import MIMEText
        #163邮箱服务器地址
        mail_host = 'smtp.126.com'  
        #163用户名
        mail_user = 'cbfddt0000'  
        #密码(部分邮箱为授权码、网易就是授权码，不是登陆密码，一定要注意) 
        mail_pass = '*****'   
        #邮件发送方邮箱地址
        sender = 'cbfddt0000@126.com'  
        #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = ['415135222@qq.com']  

        #设置email信息
        #邮件内容设置
        message = MIMEText(self.msg,'plain','utf-8')
        #邮件主题       
        message['Subject'] = '爬网结果通知' 
        #发送方信息
        message['From'] = sender 
        #接受方信息     
        message['To'] = receivers[0]  

        #登录并发送邮件
        try:
            smtpObj = smtplib.SMTP() 
            #连接到服务器
            smtpObj.connect(mail_host,25)
            #登录到服务器
            smtpObj.login(mail_user,mail_pass) 
            #发送
            smtpObj.sendmail(
                sender,receivers,message.as_string()) 
            #退出
            smtpObj.quit() 
            print('success')
        except smtplib.SMTPException as e:
            print('error',e) #打印错误