#!/usr/bin/python
# -*- coding: UTF-8 -*-
class allMethod(object):
    """docstring for ClassName"""
    def __init__(self, message):
        self.message=message
        
    def WriteTo(self):
        import os
        fi=open('log.txt',mode='a')
        fi.write('%s'%(self.message))
        fi.write('\n')
        fi.close()
        #os.system('sudo chmod 777 log.txt')

    def mailto(self):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.mime.application import MIMEApplication


        HOST = "smtp.126.com"
        SUBJECT = u"官网业务服务质量周报"
        TO = "415135222@qq.com"
        FROM = "cbfddt0000@126.com"

        msg = MIMEMultipart('related')
        def addimg(src,imgid):
            fp = open(src, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            msgImage.add_header('Content-ID', imgid)
            return msgImage

        msg.attach(addimg("/home/test/python/test/weekly.png","weekly"))

        
        msgtext = MIMEText(self.message,"html","utf-8")
        msg.attach(msgtext)


        attach = MIMEApplication(open('曾柏超的简历.doc','rb').read())
        attach.add_header('Content-Disposition', 'attachment', filename="曾柏超的简历.doc")
        msg.attach(attach)


        msg['Subject'] = SUBJECT
        msg['From']=FROM
        msg['To']=TO
        try:
            server = smtplib.SMTP()
            server.connect(HOST,"25")
            #server.starttls()
            server.login("cbfddt0000@126.com","Shift962512")
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
            print("邮件发送成功！")
        except Exception as e:
            print("失败："+str(e))
