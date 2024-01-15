#Seu programa deve identificar quantas respostas de aceitação uma menina conseguiu antes do tempo terminar.

count = 0
while True:
    line = input().strip()
    if line == "timeout":
        break
    elif line == "accepted":
        count += 1
        
print(count)
