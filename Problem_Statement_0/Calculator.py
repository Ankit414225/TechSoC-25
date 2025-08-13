import math
a=float(input("Enter first no.:"))
b=float(input("Enter second no.:"))
c=input("Choose operator(+(addition),-(subtraction),*(multiply),^(exponent),sqrt(for square root),/(divison)): ")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="/"):
    if(b==0):
        print("NOT DEFINED")
    else:
        print(a/b)         
elif(c=="^"):
    if(a==0 and b==0):
        print("Indeterminant form")         
    else:
        print(a**b)
elif(c=="sqrt"):
    if(a>=0):
        print(math.sqrt(a))
    else:
        print("NOT EXIST")  
elif(c=="*"):
    print(a*b)




                  