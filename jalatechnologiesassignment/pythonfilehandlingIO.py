#1. write a program to read text from.txtfile

f=open('first.txt','r')

#2.write a program to write text into .txt file

f=open('first.txt','a')
f.write('this file isopened for writing text')
f.close()

#3. writ a prgram to read data from excel
import pandas as pd    
    
# Read the file    
data = pd.read_csv("C:/Users/Usha/Desktop/assignment/excelfie.csv", low_memory=False)    
    
# Output the number of rows    
print("Total columns: {0}".format(len(data)))    
    
# See which headers are available    
print(list(data))

#4. program to write data into excel

import xlsxwriter     
      
book = xlsxwriter.Workbook('C:/Users/Usha/Desktop/assignment/first.xlsx')     
sheet = book.add_worksheet()     
           
sheet.write('A1','jhon')
sheet.write('B1',787)
#sheet.write('c5','amhd') 
          
book.close()     


