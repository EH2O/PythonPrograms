import time
st = time.time()
f = open("LoremIpsum.txt", "r")
text = " " + f.read()
count = 0

revText = ""
for i in range(len(text)):
    if text[i] == 'a':
        count += 1
et = time.time()
print(et-st)
print(count)

time.sleep(3)

