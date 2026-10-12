queue = [10,20,30,40,50]
stack = []
K = 3

for i  in range(K):
    stack.append(queue.pop(0))

while len(stack)>0:
    queue.append(stack.pop())

for i in range(len(queue) - K):
    queue.append(queue.pop(0))

print(queue)