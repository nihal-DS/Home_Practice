from collections import deque
d = deque(list(range(100)))
import time
start = time.time()
d.insert(9, 'hi')
end = time.time()
print(end-start)
print(len(list(d)))