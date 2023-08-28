if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    hash_value=tuple(integer_list)
    print(hash(hash_value))
