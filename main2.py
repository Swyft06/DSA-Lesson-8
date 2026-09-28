queue = ["Alice","Bob","Charlie"]
queue.append("David")
print(queue)
while len(queue) > 0:
    print(queue[0],"bought a ticket.")
    queue.pop(0)


