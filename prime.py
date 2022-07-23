start=input("start:")
s=int(start)
end=input("End:")
e=int(end)
for i in range(s,e+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)