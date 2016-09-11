def total_data(dict1, dict2):
    total = dict()
    for key in dict1:
        if key in dict2:
            total[key] = int(dict1[key]) + int(dict2[key])
        else:
            total[key] = dict1[key]
    for key in dict2:
        if key not in total:
            total[key] = dict2[key]
    return total
def main():
    a_list=list()
    for name,score in total_dict.items():
        a_list.append((name,score))
    a_list.sort()
    print ('{:10s}'.format('Name'),'{:10s}'.format('Total'))
    for i in a_list:
        print ('{:10s}'.format(i[0]),'{:<10d}'.format(int(i[1])))
first_file=open('data1.txt')
second_file=open('data2.txt')
name_list1=[]
name_list2=[]
score_list1=[]
score_list2=[]
for i in first_file:
    if 'Name' in i:
        continue
    i=i.strip()
    i=i.split()
    name_list1.append(i[0])
    score_list1.append(i[1])
dict1=dict(zip(name_list1,score_list1))
for i in second_file:
    if 'Name' in i:
        continue
    i=i.strip()
    i=i.split()
    name_list2.append(i[0])
    score_list2.append(i[1])
dict2=dict(zip(name_list2,score_list2))
total_dict=total_data(dict1,dict2)
main()
