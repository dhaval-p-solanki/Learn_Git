'''
#Smallest num from Array
arr=[10,20,60,50,5]
a=min(arr)
print(a)

#reverse a given array
arr=[10,20,30,40,50]
#arr.reverse()       #Array Descending Order
arr=arr[::-1]
print(arr)
a=sorted(arr)      #Array Ascending Order
print(a)

#count the frequency of each element in array
arr=[10,20,30,40,50,20]
freq={}

for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)


##sum of arr
arr=[10,20]
a=sum(arr)
print(a)
##total=0
##for i in arr:
##    total+=i
##print(total)


#intermedian of arr element
def freq_arr(arr):
    arr.sort()
    n=len(arr)

    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2])/2
    return median

arr=[10,20,50,40,30]
median=freq_arr(arr)
print(median)


#remove duplicate Element from array
shorted_arr=[]
a=int(input("Enter num of ele = "))

for i in range(a):
    value=input(f"Enter num {i+1} = ")
    shorted_arr.append(value)

a=set(shorted_arr)
short=sorted(a)
print(short)

#replace each element in the array by its rank in the array
def sort_arr(arr):
    s=sorted(arr)
    freq={}
    index=1
    for i in s:
        if i not in freq:
            freq[i]=index
            index+=1
    return freq

arr=[50,10,20,30]
short=sort_arr(arr)
print("array by its rank = ",short)


##rotate the elements of an array (left to right)
def rotate(arr,k):
    n=len(arr)
    k=k%n

    for i in range(n):
        rotate_ele = arr[k:] + arr[:k]
    return rotate_ele

arr=[10,30,20,50]
k=1
x=rotate(arr,k)
print(x)

#search for an element in an array 
def find(arr,k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

arr=[10,30,20,50]
k=50
x=find(arr,k)
if x != -1:
    print(f"{k} is on index {x}")
else:
    print(f"{k} index {x} not found")
'''
#====================================================================================================================
'''
# Fibonacci Serice    ==========================
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n=7
for i in range(n):
    print(fibo(i))    


#prime number ==========================
def prime(n):
    if n <= 1:
        return n
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=3
if prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

# Palindrome    ==============================
n=121
original=str(n)
rev=original[ : : -1]
if original == rev:
    print("palindrome")
else:
    print("not palindrome")


# Factorials ==========================
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n *  fact(n-1)

n=5
f=fact(n)
print(f)


#armstrong number
def arm(num):
    digits=str(num)
    power=len(digits)

    sum_arm=sum(int(digit) ** power for digit in digits)
    return sum_arm == num

n=153
if arm(n):
    print(f"{n} is arm")
else:
    print(f"{n} not arm")


#sum of digit
def digit(n):
##    total=0
##    for i in str(n):
##        total+=int(i)
##    return total
    #return sum(int(total) for total in str(n))         # 2nd Way

n=153
result=digit(n)
print(result)


#swep 2 num
a=1
b=2
a=a+b
b=a-b
a=a-b
##a = a^b
##b = a^b
##a = a^b
print("a = ",a)
print("b = ",b)


#bubble short
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[10,23,56,89,12,22,14,1]
bubble(arr)
print(arr)
'''

