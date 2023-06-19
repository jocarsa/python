import time

einicio = int(time.time())
n = 1.0000000064
for i in range (0,100000000):
    n *= 1.00000000065

efinal = int(time.time())
print(efinal-einicio)
