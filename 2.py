# Program 1

#List --> to store more than one value
a = ["Vasudha","Dilip","Mamata","Wankhade","Namrata","Jagtap","Harshal","Sanjivani","Anu","Kiran"]
print(a[0])
print(a[2])

# Slicing a[start:end:steps]

print(a[1:5])
print(a[0:9:2])
print(a[::-1]) # reverse

# Program 2

# Basic for loop

companies = ["HCL","Infosys","Capgemini","Cognizant","Dell"]
# print each element separately
for item in companies:
    print(item)

# using range 
for y in range(10):
    print(y)

flowers = ["Marigold","Rose","Jasmine","Lily"]
l = len(flowers)
# print each element separately
for x in range(0,l):
    print(flowers[x])  


# Program 3 --> some methods of list

aa = [1,2,3,4,4,5,6,7,8]
print(aa)

# 1) index() --> gives first index of specific element
inx = aa.index(4)
print(inx)

# 2) reverse() --> to reverse list and returns none
rev = aa.reverse()
print(rev)
print(aa)

# 3) pop() --> to delete last element and returns same element
delete = aa.pop()
print(delete)
print(aa)

# 4) remove() --> to remove specific element and returns none
fruits = ["Apple","Mango","Grapes"]
rm = fruits.remove("Mango")
print(rm)
print(fruits)

# 5) concatenation of two lists
ab = [12,3,23,4]
bd = [12,3,23,3,4]
print(ab+bd)

# 6) to repeat elements in list required number of times
f = [111,222,3333]
print(f*2)

# 7) append() --> to add element at the end of list and returns none
r = [11,22,33,44,55,66]
app = r.append(100)
print(app)
print(r)

# 8) insert() --> to add element at specific index and returns none
t = [1,2,3,4,5,6]
tt = t.insert(3,"Vasudha") 
print(tt)
print(t)

# 9) max() and min() --> to get maximum and minimum element in list
# o = [11,2,44,55]
# oo =o.max(o)
# print(oo)
# ooo = o.min(o)
# print(ooo)