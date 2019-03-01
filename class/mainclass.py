#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
class WriteToLog(object):
    #def __init__(self, msg):
    #    self.msg=msg
    def WriteTo(self,msg):
        fi=open('log.txt',mode='a')
        fi.write('%s'%(msg))
        fi.write('\n')
        fi.close()
        os.system('sudo chmod 777 log.txt')


#x=WriteToLog().WriteTo('dog')

