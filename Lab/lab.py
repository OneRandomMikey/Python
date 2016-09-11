# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 18:29:04 2016

@author: Zehua Li
"""

open_file=open('data.txt')
count=0
for i in open_file:
    element=i.split()
    name_str=element[0]
    height=element[1]
    #print (type(height))
    score_list=[]
    
    if count>0:
        h=''
        for i in element[1:]:
            h+=i
            score_list.append(h)
            score_list+=score_list
        #score_list.sort()
        height=score_list[0].split()
        for i in height:
            
            print (i)
        #height.sort()
        
        #print(my_list)
        #height=0
        ##number=element[1]
       # print (number)
        
      #  print(type(score_list[0]))
    else:
        count+=1