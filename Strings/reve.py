import time
st = time.time()
f = open("LoremIpsum.txt", "r")
text = " " + f.read()


revText = ""
for i in range(len(text)):
    revText += text[len(text)-i-1]
et = time.time()
print(et-st)

time.sleep(3)

