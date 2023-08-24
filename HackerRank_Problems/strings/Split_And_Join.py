

def split_and_join(line):
    # write your code here
    return "-".join(line1)

if __name__ == '__main__':
    line = input()
    line1= line.split()
    result = split_and_join(line1)
    
    print(result)