# exercise from section 4, integer base
# write algorithm, i.e.as a function, that takes in an integer base 10 and a base in which it should be represented and gives out the representation in that base,
# next step, write a function that maps from the digit of that representation to a fitting encoding, i.e. 12 in base 12 is c.

# so: ?
# take floor of input number by base and put mod back as number
# stop when floor == 0

def from_base10(n,b):
    if b<2:
        raise ValueError('b should be >=2')
    if n<0:
        raise ValueError('n should be positive')
    if n==0:
        raturn [0]
    
    digits=[]
    
    while n >0:
        m = n%b
        n = n//b
        #n,m = divmod(n,b) alternative way
        digits.insert(0,m)
    
    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit map not ong enough")
    
    encoding=''.join([digit_map[d] for d in digits])
    return encoding


# put together in one fct.:

def rebase_from10(number, base):
    digit_map='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base <2 or base >36:
        raise ValueError("rong base size")
    
    sign= -1 if number <0 else 1 #<-- explre why
    number*=sign
    
    digits = from_base10(number,base)
    encoding = encode(digits, digit_map)
    
    if sign== -1:
        encoding= '-' + encoding
    
    return encoding
    

inp=input("enter number and to.be.converted-to base in the form <<number,base>>")

inp=inp.split(",")
n=int(inp[0])
b=int(inp[1])

print(rebase_from10(n,b))
