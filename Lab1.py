#Lab 1: assisgement to practice for basic synatx: formating print, string, etc"
#Name: Peicong Wu
#Date: 04/20/2020
import datetime

CO_UNT = 1
print("=" * 40 )
myName = "Peicong Wu"
myString1 = "Lab " + str(CO_UNT)
width = int((40-len(myName))/2)
print(" " * width + myName)
width = int((40-len(myString1))/2)
print(" " * width + myString1)
print("=" * 40 )
print("\n")
now = datetime.datetime.now()
diff = datetime.date(now.year, now.month, now.day)- datetime.date(2020, 3, 18)
print("Today is ", now.month,"/",now.day,"/",now.year, sep="")
print("It's been",diff.days,"days we use zoom for learning.")

""""
Output
========================================
               Peicong Wu
                 Lab 1
========================================


Today is 4/20/2020
It's been 33 days we use zoom for learning.
"""
