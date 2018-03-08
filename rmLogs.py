#encoding:utf-8
import os
import glob
import time
import datetime
class DeleteLogfile(object):

        def __init__(self,filename='*.txt',days=5,path='D:/test',logs='logs.log'): # 文件类型/删除时间/文件目录
                self.__filename = filename
                self.__days = days
                self.__path = path
                self.__logs = logs

        def delete(self):
                xDate = (datetime.datetime.now() - datetime.timedelta(days = self.__days))
                files = glob.glob(self.__path+'/'+self.__filename)
                for log in files:
                        stats=os.stat(log)
                        lastmodDate = time.localtime(stats[8])
                        expDate = xDate.strftime('%Y-%m-%d')
                        expDate = time.strptime(expDate, '%Y-%m-%d')
                        print log, time.strftime("%m/%d/%y", lastmodDate)
                        if expDate > lastmodDate:
                                try:
                                        print ('Removing', log, time.strftime("(older than %m/%d/%y)", expDate))
                                        # file = self.__path + '/' + self.__logs
                                        # if not os.path.exists(file):
                                        #         fobj = open(file, 'w')
                                        #         fobj.close()
                                        # mopen = open(file, 'r+')
                                        # data = mopen.readlines()
                                        # data.insert(len(data) + 1,
                                        #             'Removing '+log+' '+time.strftime("(before %m/%d/%y)", expDate)+ os.linesep)
                                        # mopen = open(file, 'w+')
                                        # mopen.writelines(data)
                                        # mopen.close()
                                        os.remove(log)
                                except OSError:
                                        print ('Could not remove', log)

if __name__ == '__main__':
        obj = DeleteLogfile()
        obj.delete()
