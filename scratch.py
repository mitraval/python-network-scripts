numbers = [1,2,3,4,5]
num = numbers[1:4]
print(f'nums:{num}')
print(f'numbers:{numbers}')
print(numbers[:3])
print(numbers[2:])
print(numbers[1:5:3])
print(numbers[4:1:-2])
print(numbers[::]) # will print entire list
print(numbers[::-1])   # will print list in the reverse order
numbers[0:2] = ['a', 'b'] # slicing will change the list
print(numbers)
#numbers[0:2] = ['x,'y','z']
print(numbers)

ip_list = ['192.168.1.1', '192.168.1.2', '192.168.1.4']
for ip in ip_list:
    print(f'connecting to {ip}')
print('192.168.1.1' in ip_list)  # it will return true , because ip is inluded in the list
print('192.156.66.1'  in ip_list)  # will return false
