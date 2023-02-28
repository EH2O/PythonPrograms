import time
x = 3.2
y = 7.5
z = x*y
st = time.time()
for i in range(100000000):
    if z < i:
        z = z*x
    else:
        z = z/y

et = time.time()
deltaTime = et-st
print(deltaTime, ":", x)
time.sleep(4)