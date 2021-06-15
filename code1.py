word = input()
middle = len(word)//2
converted = word[middle:]+word[:middle]
k = 2*len(word)-2
for i in range(0,len(word)):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print(converted[j]+" ",end="")
    print("\r")
