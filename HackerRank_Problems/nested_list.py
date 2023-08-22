# final submission

student_list=[]
score_list=[]
if __name__ == '__main__':
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])
        score_list.append(score)
    b=sorted(set(score_list)) [1]

    for a, c in sorted(student_list):
        if c==b:
            print (a)


#just rough
# print(list2[1])
# print(list[0][1])
# print(sorted(list[]))


#https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/


#today i learnt

#how to use nested list
#how to intialize and access nested list
#how to sort nested list
