open_file=open('data.txt')
temp_file=open('output.txt','w')
count=0
min_height=10000
max_height=0
sum_height=0
min_weight=10000
max_weight=0
sum_weight=0
min_bmi=10000
max_bmi=0
sum_bmi=0
for line in open_file:
    line=line.strip()
    elements_data=line.split()
    name=elements_data[0]

    if count>0:
        height=float(elements_data[1])
        weight=float(elements_data[2])
        bmi=weight/height**2
        if bmi<min_bmi:
            min_bmi=bmi
        if bmi>max_bmi:
            max_bmi=bmi
        sum_bmi+=bmi
        avg_bmi=sum_bmi/8

        if height<min_height:
            min_height=height
        if height>max_height:
            max_height=height
        sum_height+=height
        avg_height=sum_height/8
        if weight<min_weight:
            min_weight=weight
        if weight>max_weight:
            max_weight=weight
        sum_weight+=weight
        avg_weight=sum_weight/8
        print (line,'{:10.2f}'.format(bmi),file=temp_file)
    else:
        count+=1
        print (line,'BMI',file=temp_file)
print('{:s}{:9.2f}{:13.2f}{:11.2f}{:s}{:13.2f}{:13.2f}{:11.2f}{:s}{:13.2f}{:13.2f}{:11.2f}'.format('\nAverage',avg_height,avg_weight,avg_bmi,'\nMax',max_height,max_weight,max_bmi,'\nMin',min_height,min_weight,min_bmi),file=temp_file)
open_file.close()
temp_file.close()
