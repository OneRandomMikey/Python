#Computer Project #04
#section 730
#June 13, 2016
#define 4 new function and find the print the highest 6 averages (for the column selected) and the lowest 6 averages. Print that
#data with the month-year information.
# get_input_descriptor is to open the file
def get_input_descriptor():
    while True:
        try:
            file_open=open(input('\nOpen what file:'))
            break
        except:
            print('\nPlease enter a corret filename')
            continue
    return file_open
#get_data_list is to open the file by column
def get_data_list(fp,c,x=0):
    result=[]
    for line in fp:
        #get rid off first line
        if x==0:
            x+=1
            continue
        else:
            line=line.strip()
            line_lst=line.split(',')
            date=line_lst[0]
            data=line_lst[c]
            element_tuple=date,data,
            result.append(element_tuple)
    #return a list
    return result
# find the average of the each month
def average_data(list_of_tuples):
    month=['January','February','March','April','May','June','July','August','September','October','Novermber','December']
    current_month=''
    current_ear=''
    sum_value=0
    time=0
    result=[]
    for i in list_of_tuples:
        date=i[0]
        new_year=date[0:4]
        new_month=date[4:6]
        if new_month!= current_month:
            if current_month=='':
                current_month=new_month
                current_year=new_year
                sum_value+=float(i[1])
                time+=1
                continue
            int_month=int(current_month)
            avg_value=float(sum_value/time),str(month[int_month-1]+' '+current_year)
            current_month=new_month
            current_year=new_year
            sum_value=0
            time=0
            #creat a list
            result.append(avg_value)
        sum_value+=float(i[1])
        time+=1
    int_month=int(current_month)
    avg_value=float(sum_value/time),str(month[int_month-1]+' '+current_year)
    #creat a list
    result.append(avg_value)
    #return a list
    return result
# list 6 lowest value and 6 height value
def main():
    fp1=get_input_descriptor()
    col=int(input('\nWhat column:'))
    c=get_data_list(fp1,col)
    avg=average_data(c)
    avg.sort()
    print('\nLowest 6 for column',col)
    #find 6 lowest value
    for i in avg[0:6]:
        time=str(i[1])
        avg_value=i[0]
        print('Date:''{:>15s}'.format(time),',','Value:','{:10.2f}'.format(avg_value))
    print('\nHightest 6 for column',col)
    #find 6 heightest value
    for i in avg[-1:-7:-1]:
        time=str(i[1])
        avg_value=i[0]
        print('Date:''{:>15s}'.format(time),',','Value:','{:10.2f}'.format(avg_value))
    fp1.close()
main()
