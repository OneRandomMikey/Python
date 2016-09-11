vowels='aeiouy'
op_file=open("dictionary.txt",'r')
for line in op_file:
    count=0
    if line[0].isupper():
        continue
    else:
        if len(line)!=8:
            continue
        else:
            if 's' in line:
                continue
            else:
                for x in line:
                    if x in vowels:
                        count+=1
                if count==1:
                    print (line)
op_file.close()




def calculate_line(line_str):
    elements_list=line_str.split()
    name_str=elements_list[0]
    score_list=[]
    for score in elements_list[1:]:
        score_list.append(int(score))
    score_list.sort()
    max_int=score_list[-1]
    min_int=score_list[0]
    avg_float=sum(score_list)/len(score_list)
    return name_str,max_int,min_int,avg_float
def main():
    f_obj=open('data.txt')
    for line in f_obj:
        line=line.strip()
        if line:
            result_tuple=calculate_line(line)
            print('{:>6s} {:4d} {:4d} {:7.2f}'.format(reuslt_tuple[0],result_tuple[1],result_tuple[2],result_tuple[3]))
    f_obj.close()
print (main())
