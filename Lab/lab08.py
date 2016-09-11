open_file=open(input('Please input a file name:'))
a_list=[]
score_1=0
score_2=0
print('{:20s}'.format('Name'),'{:26s}'.format('Exam1 Score'),'{:26s}'.format('Exam2 Score'))
for line in open_file:
    line=line.strip()
    element=line.split()
    name=element[0]+element[1]
    name_str=str(name)
    score1=int(element[2])
    score2=int(element[3])
    element_tuple=name,score1,score2
    a_list.append(element_tuple)
a_list.sort()
for i in a_list:
    name_str=str(i[0])
    score1=int(i[1])
    score2=int(i[2])
    score_1+=score1
    score_2+=score2
    print('{:20s}'.format(name_str),'{:<26d}'.format(score1),'{:<26d}'.format(score2))
avg_score1=score_1/5
avg_score2=score_2/5
print('{:21s}'.format('\nAverage of scores'),'{:<26.1f}'.format(avg_score1),'{:<26.1f}'.format(avg_score2))
