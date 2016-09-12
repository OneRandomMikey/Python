def get_input_descriptor():
    while True:
        try:
            fp=open(input('\nOpen what file:'))
            break
        except:
            print('\nPlease enter a corret filename')
            continue
    return fp

def get_data_list(fp,c,x=0):
    result=[]
    for line in fp:
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
    return result

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
            result.append(avg_value)
        sum_value+=float(i[1])
        time+=1
    int_month=int(current_month)
    avg_value=float(sum_value/time),str(month[int_month-1]+' '+current_year)
    result.append(avg_value)
    return result



def main():
    fp1=get_input_descriptor()
    col=int(input('\nWhat column:'))
    c=get_data_list(fp1,col)
    avg=average_data(c)
    avg.sort()
    print('\nLowest 6 for column',col)
    for i in avg[0:6]:
        time=str(i[1])
        avg_value=float(i[0])
        print('Date:''{:>15s}'.format(time),',','Value:','{:10.2f}'.format(avg_value))
    print('\nHightest 6 for column',col)
    for i in avg[-1:-7:-1]:

        time=str(i[1])
        avg_value=float(i[0])
        print('Date:''{:>15s}'.format(time),',','Value:','{:10.2f}'.format(avg_value))

main()






    month_year=['January','February','March','April','May','June','July','August','September','October','Novermber','December']
    month=0
    count=0
    sum_data=0
    count_data=0
    result=[]
    for i in list_of_tuples:
        date=i[0]
        current_month=int(date[4:6])
        current_year=int(date[0:4])
        if month!=current_month and count_data==0:
            month=current_month
            count_data+=1
        if current_month==month:
            sum_data+=float(i[1])
            count+=1
        if month!=current_month:
            month=current_month
            avg_sum=float(sum_data/count)
            if current_month==1:
                element_tuple=avg_sum,str(month_year[current_month-2])+' '+str(current_year-1)
            else:
                element_tuple=avg_sum,str(month_year[current_month-2])+' '+str(current_year)
            result.append(element_tuple)
            count=0
            sum_data=0
            avg_sum=0
    avg_sum=float(sum_data/count)
    element_tuple=avg_sum,str(month_year[current_month-1])+' '+str(current_year)
    result.append(element_tuple)
    return result
