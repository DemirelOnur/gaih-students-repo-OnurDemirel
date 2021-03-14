even=[0,2,4,6,8]
odd=[1,3,5,7,9]
num=even+odd

x = range((len(num)))
for i in x:
    num[i]*=2
    print("Number: %d, tipi:"% num[i], type(num[i]))