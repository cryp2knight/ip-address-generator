devs = []
while True:
    inp = input("No. of PCs: ")
    if inp != "":
        devs.append(int(inp))
    else:
        break

devs.sort()
devs.reverse()
print(devs)

def checkRange(num):
    val = None
    bits = [1,2,4,8,16,32,64,128,256]
    for i in bits:
        if num <= i-2:
            val = i
            break
    return val

counter = 0
print("NA    1st   Lst   BIP   Sub  ")
for dev in devs:
    ss = counter+checkRange(dev)
    first = counter + 1
    print('{:<6d}{:<6d}{:<6d}{:<6d}{:<6d}'.format(counter,first,ss-2,ss-1,256-checkRange(dev)))
    counter = ss





