player = ["a","b","c","d","e"]

while len(player) > 1:
    for i in range(2):
        player.append(player.pop(0))

    out = player.pop(0)
    print(out,"is out")
        

print("Winner is ",player[0])
