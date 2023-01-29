# Maximum sum of subarray of length k (Sliding window problem 1)
# https://youtu.be/KtpqeN0Goro
x = [0,1,2,3,4,5]   #len-k+1
k = 3
max1 = 0
ini = sum(x[0:k])
for i in range(len(x)-k+1): #4
    ini = ini - x[i] + x[k-1+i]
    max1 = max(max1, ini)
print(max1)