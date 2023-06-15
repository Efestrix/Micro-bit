
def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    if index>1:
        return fibonacci(index-1)+fibonacci(index-2)

for i in range(10):
    print(fibonacci(i))
