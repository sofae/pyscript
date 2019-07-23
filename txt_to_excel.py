#coding=utf-8
#######################################################
#filename:txt2excel.py
#author:Delfy
#date:2016-7-8
#function：读取txt导入excel文件
#######################################################
import xlwt
from datetime import datetime

row=0
column=['代码','交易状态','返回码','日期','分组号','商户名','打款金额','帐号','帐号名','开户行','流水号','流水号','流水号']

wb = xlwt.Workbook(encoding='gbk',style_compression=0)
ws = wb.add_sheet('RECEIPT',cell_overwrite_ok=True)
for i in range(0,len(column)):
    ws.write(0,i,column[i].decode('utf8'))


f = open(r'f:\8804-'+datetime.now().date().strftime('%Y%m%d')+'.txt')
line = f.readline()
while line:
    yline = line.split('|')
    line = f.readline()

    row=row+1

    for i in range(0,len(column)):
        ws.write(row,i,yline[i])


    
        
#保存该excel文件,有同名文件时直接覆盖
wb.save('f:\\test.xls')
print '创建excel文件完成！'
