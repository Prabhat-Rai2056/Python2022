courses=['python', 'c', 'c++']
fir=input('press a for add and d for delete in this list:')
if fir == 'a':
    num=input('how many data do you want to add:')
    n=int(num)
    for new in range(n):
        new=input('enter the value: ')
        courses.append(new)
    print(courses)
elif fir == 'd':
    rem=input("what do you want to delete:")
    x=str(rem)
    courses.remove(x)
    print(courses)
else:
    print("please enter correct option")
