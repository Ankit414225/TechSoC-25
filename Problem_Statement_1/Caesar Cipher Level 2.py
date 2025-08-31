from collections import Counter
alphabet_freq={
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7,
    'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2,
    'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5,
    'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1,
    'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0,
    'z': 0.1
} 
def decode(cipher_text,shift):
    result=[]
    for c in cipher_text:
        if c.isalpha():
            if c.isupper():
                base=ord('A')
            else:
                base=ord('a')    

            shifted=(ord(c)-base-shift)%26+base
            result.append(chr(shifted))  
        else:
            result.append(c)      
    return ''.join(result)
def letter_freq(text):
    letters=[]
    for c in text:
        if c.isalpha():
            letters.append(c.lower())
    return Counter(letters)

def score_of_text(text):
    freq=letter_freq(text)
    total=sum(freq.values())
    if total==0:
        return float("invalid")
    score=0
    for letter,expected in alphabet_freq.items():
        observed=(freq.get(letter,0)/total)*100
        score+=(observed-expected)**2/expected
    return score
def casear_breaker(cipher_text):
    best_shift=None
    best_score=float("inf")
    best_message=""
    for shift in range(1,26):
        candidate=decode(cipher_text,shift)
        current_score=score_of_text(candidate)
        if(current_score<best_score):
            best_score=current_score
            best_shift=shift
            best_message=candidate
    return best_message,best_shift
cipher_text=input()       
decoded_message,shift_used=casear_breaker(cipher_text) 
print("HIDDEN MESSAGE:",decoded_message)
print("Shift used:",shift_used)