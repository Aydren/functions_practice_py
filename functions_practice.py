def hello():
    return

print(hello())

def pack(a, b, c):
    return [a, b, c]

print(pack('list 1', 'list 2', 'list 3'))


my_list = ['sushi', 'spam masubi']

def eat_lunch(list):
    if len(list) == 2:
        print(f"First I eat {list[0]}, Next I eat {list[1]}")
        #extra elif just for fun
    elif len(list) == 1:
        print(f'I only eat {list[0]} for today')
    else:
        print('My lunch box is empty')

eat_lunch(my_list)
