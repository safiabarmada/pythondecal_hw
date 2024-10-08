def computePower(x,y):
    i = 1
    for f in range(y):
        i *= x
    return i
print(computePower(2,3))

readings = [15, 14, 17, 20, 23, 28, 20]
temperatureRange = (min(readings),max(readings))
print(temperatureRange)

def isWeekend(day):
    if day in range(6,8):
        return True
    elif day in range (1,6):
        return False
print(isWeekend(7))

distance = 70
fuel = 21.5
def fuel_efficiency(distance, fuel):
    return distance / fuel
print(fuel_efficiency(distance, fuel))

def decodenums(n):
    import math
    digits = int(math.log10(n))
    a = n//10
    b = n%10
    c = 10**digits
    return (b*c + a)
print(decodenums(12345))

nums = [98, 2024, 131, 2, 3, 72]
max = nums[0]
for number in nums:
     if number>max:
          max = number
min = nums[0]
for number in nums:
     if number<min:
           min = number
print(min,max)

max_w = nums[0]
i=0
while i<len(nums):
    if max_w<nums[i]:
        max_w = nums[i]
    i = i+1
min_w = nums[0]
i=0
while i<len(nums):
    if min_w > nums[i]:
        min_w = nums[i]
    i = i +1
print(min_w,max_w)


text = "UC Berkeley founded in 1868!"
def vc_count(text):
    count_v = 0
    for char in text:
        if char in "aeiouAEIOU":
            count_v = count_v + 1
    count_c = 0
    for char in text:
        if char in "qwrtyplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXCVBNM":
            count_c = count_c + 1
    return (count_v, count_c)
print(vc_count(text))

num = 2468
import math
digits = int(math.log10(num))
digit_list=[]
for i in range (0,digits+1):
    digit=num//(10**(digits-i)) - ((10)*(num//(10**(digits+1-i))))
    i = i+1
    digit_list.append(digit)
print(sum(digit_list))