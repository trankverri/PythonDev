# n=int(input("input number"))
# a0=0
# a1=1
# for i in range(n):
#     print(a0, end=' ')
#     x=a0+a1
#     a0=a1
#     a1=x
# #
# a0=0; a1=1; i=2; x=1
# while a0<=n:
#     x=a0+a1; a0=a1
#     a1=x
#     i+=1
#     if x >n:
#         i=0
# if i!=0:
#     print(i)
# else:
#     print (-1)
    
#
k=int(input("введите количество арбузов"))
x= int(input("massa: "))
min_massa, max_massa=x,x
for i in range(k-1):
    x= int(input("massa: "))
    if x> max_massa:
        max_massa=x
    elif x< min_massa:
        min_massa=x
print (min_massa, max_massa)
        
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
list_2 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
list_3 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
list_4 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]

# делим шоколадку на "с" долек
a = 5
b = 3
c = 11

if (c>=a or c>=b) and (c==(a*b)-a or c==(a*b)-b):
#if c <= b * a and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")
    
    