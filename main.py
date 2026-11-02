class Stack:
    def __init__(self):
        self.__arr = []
        
    def is_empty(self):
        return len(self.__arr) == 0
        
    def push(self, n):
        self.__arr.append(n)
    
    def pop(self):
        return self.__arr.pop(-1)
    
    def peek(self):
        return self.__arr[-1] 

def factorial(n):
    if n < 0:
        raise ValueError('Факториал принимает только положительные числа')
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def list_sum(arr):
    arr_len = len(arr)
    if arr_len <= 0:
        return 0
    if arr_len == 1:
        return arr[0]
    return arr[0] + list_sum(arr[1:])


def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
print(factorial(5))
print(list_sum(arr))
print(binary_search(arr, 3))

stack = Stack()
stack.push(2)
stack.push(5)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())