#Computer Project #05
#section 730
#June 20, 2016
#open three files
#find Government employment average per month
#find Private employment average per month
#find Private Employment by president
#find Government Employment by president

# return list for dem, rep and presidents
def year():
    presidents_list=[]
    D={}
    dem_year_list=[]
    rep_year_list=[]
    for line in fp_presidents:
        line_lst=line.strip().split(', ')
        presidents_list.append(line_lst)
        date=(line_lst[0])
        D[date]=line_lst[1:]
        if len(line_lst)>3:
            if 'Democrat' in line_lst:
                for i in range(int(line_lst[2][0:4]),int(line_lst[2][5:])):
                    dem_year_list.append(i)
            if 'Republican' in line_lst:
                for i in range(int(line_lst[2][0:4]),int(line_lst[2][5:])):
                    rep_year_list.append(i)
            continue
        if 'Democrat' in line_lst:
            for i in range(int(line_lst[1][0:4]),int(line_lst[1][5:])):
                dem_year_list.append(i)
        if 'Republican' in line_lst:
            for i in range(int(line_lst[1][0:4]),int(line_lst[1][5:])):
                rep_year_list.append(i)
    return dem_year_list,rep_year_list,presidents_list
#return avg for dem and rep, also return the list for two data files
def avg(fp):
    D={}
    data_list=[]
    for line in fp:
        line_lst=line.strip().split(',')
        if 'Year' in line_lst:
            continue
        data_list.append(line_lst)
        date=int(line_lst[0])
        D[date]=line_lst[1:]
    dem_total=0
    rep_total=0
    for key in D:
        if key in dem_year_list:
            for month in range(12):
                dem_total+=int(D[key][month])
        if key in rep_year_list:
            for month in range(12):
                rep_total+=int(D[key][month])
    return dem_total/(len(dem_year_list)*12),rep_total/(len(rep_year_list)*12),data_list
# find the data for each presidents
def difference(data_list):
    if data_list==private_data_list:
        print('\nprivate Employment by president (millions)','{:12s}'.format('\nPresident'),\
        '{:14s}'.format('First Month'),'{:13s}'.format('Last Month'),'{:13s}'.format('Difference'),\
        '{:13s}'.format('Percentage'))
    if data_list==government_data_list:
        print('\nGovernment Employment by president (millions)','{:12s}'.format('\nPresident'),\
        '{:14s}'.format('First Month'),'{:13s}'.format('Last Month'),'{:13s}'.format('Difference'),\
        '{:13s}'.format('Percentage'))
    for line in presidents_list:
        name=''
        reverse_line=line[0][::-1]
        for letter in reverse_line:
            if letter !=' ':
                name+=letter
            else:
                break
        name=name[::-1]
        if len(line)>3:
            for data in data_list:
                if line[2][0:4] in data:
                    first_month=int(data[1])
                if str(int(line[2][5:])-1) in data:
                    last_month=int(data[-1])
                    difference=last_month-first_month
                    print('{:10s}'.format(name),'{:12,d}'.format(first_month),'{:13,d}'.format(last_month),\
                    '{:13,d}'.format(difference),'{:13.1%}'.format(difference/first_month))
        else:
            for data in data_list:
                if line[1][0:4] in data:
                    first_month=int(data[1])
                last_year=str(int(line[1][5:])-1)
                if last_year in data:
                    last_month=int(data[-1])
                    difference=last_month-first_month
                    print('{:10s}'.format(name),'{:12,d}'.format(first_month),'{:13,d}'.format(last_month),\
                    '{:13,d}'.format(difference),'{:13.1%}'.format(difference/first_month))
# open file and do error checking
while True:
    try:
        fp_presidents=open(input('Please enter a file name for presidents:'))
        break
    except:
        print('***********incorrect file name***********')
        continue
while True:
    try:
        fp_private=open(input('Please enter a file name for private_employment:'))
        break
    except:
        print('***********incorrect file name***********')
        continue
while True:
    try:
        fp_government=open(input('Please enter a file name for government_employment:'))
        break
    except:
        print('***********incorrect file name***********')
        continue

year=year()
dem_year_list=year[0]
rep_year_list=year[1]
presidents_list=year[2]

avg_government=avg(fp_government)
avg_private=avg(fp_private)
avg_dem_government=avg_government[0]
avg_rep_government=avg_government[1]
avg_dem_private=avg_private[0]
avg_rep_private=avg_private[1]
government_data_list=avg_government[2]
private_data_list=avg_private[2]

print('Gvoernment employment average per month (millions)',\
'\nRepublican:','{:10,d}'.format(int(avg_rep_government)),'\nDemocratic:','{:10,d}'.format(int(avg_dem_government)))
print('Private employment average per month (millions)',\
'\nRepublican:','{:10,d}'.format(int(avg_rep_private)),'\nDemocratic:','{:10,d}'.format(int(avg_dem_private)))


difference(private_data_list)
difference(government_data_list)
fp_presidents.close()
fp_private.close()
fp_government.close()
