import time

x = 3
y = 7

st = time.time()
for i in range(100000000):
    if i % 2 == 0:
        x += 203455
    else:
        x -= 203455

et = time.time()
deltaTime = et - st
print(deltaTime, ":", x)
time.sleep(4)
