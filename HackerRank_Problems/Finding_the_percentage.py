if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    total=0
    for ele in range(0, len(scores)):
       total= float(total + scores[ele])
    
    avg=(total/len(scores))
    print(f"{avg:.2f}")

    
    # today i learnt 

    # .2f is used for rounding of number to 2 decimal points
    # how to sum elements in list.
    
