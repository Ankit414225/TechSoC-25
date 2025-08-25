name=input("Enter a word:") 
# Take the shift value (number of positions to shift characters)               
shift=int(input())
encoded=""   # Empty string to store encoded text
if shift>=0 and shift<26:
    for val in name:  
        x=ord(val)   # Convert character to its ASCII value
        n=x+shift
        encoded+=chr(n)
        if(x<=90 and x>=65):           # If character is uppercase A–Z
            if (n<=90 and n>=65) :   # Wrap around if it goes past 'Z'
                
                print(chr(n),end=" ")    
            elif (n>90) :
            
                n-=26
                print(chr(n),end=" ")
            elif(n<65):
                n+=26
                print(chr(n),end=" ")
        elif(x>=97 and x<=122):    # If character is lowercase a–z
            if (n<=122 and n>=97) :  # Wrap around if it goes past 'z'
                
                print(chr(n),end=" ")    
            elif (n>122) :
            
                n-=26
                print(chr(n),end=" ")
            elif(n<97):
                n+=26
                print(chr(n),end=" ")
        elif(x>=32 and x<=64):   # If character is not alphabet (special char, number, space)
            print(chr(x),end=" ")
print()            
a=input("For Decode press 'D':")
if(a=="D"):
    shift1=-shift   # Reverse the shift for decoding
for vl in encoded :
    k=ord(vl)
    s=k+shift1
    if(k>=65 and k<=90):    # If uppercase A–Z
        if (s<=90 and s>=65) :
                
            print(chr(s),end=" ")    
        elif (s>90 and s<=96) :
            
            s-=26
            print(chr(s),end=" ")
        elif(s<65):
            s+=26
            print(chr(s),end=" ")
    elif(k>=97 and k<=122):    # If lowercase a–z
        if (s<=122 and s>=97) :
                
            print(chr(s),end=" ")    
        elif (s>122 ) :
            
            s-=26
            print(chr(s),end=" ")
        elif(s<97):
            s+=26
            print(chr(s),end=" ")
    elif(k>=32 and k<=64):     # If not alphabet (special chars, numbers, etc.)
        print(chr(x),end=" ")

    
     
        
               