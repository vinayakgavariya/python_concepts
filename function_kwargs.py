def person(name, **data):
    # print(name)
    # print(data)

    for i,j in data.items():
        print(i,j)

person('navin',28, 'Mumbai', mob=922)