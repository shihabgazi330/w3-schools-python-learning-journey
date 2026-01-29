print("""
operation    example    same as
=	         x = 5	     x = 5	
+=	         x += 3	     x = x + 3	
-=	         x -= 3      x = x - 3	
*=	         x *= 3      x = x * 3	
/=	         x /= 3      x = x / 3	
%=	         x %= 3      x = x % 3	
//=	         x //= 3	 x = x // 3	
**=	         x **= 3	 x = x ** 3	
&=	         x &= 3	     x = x & 3	
|=	         x |= 3	     x = x | 3	
^=	         x ^= 3	     x = x ^ 3	
>>=	         x >>= 3	 x = x >> 3	
<<=	         x <<= 3	 x = x << 3	
:=	         print(x := 3)	x = 3
                            print(x)
""")


x = 0 # Assigning a value
print(x)

x += 33 # addition
print(x)
x -= 3 # deduction
print(x)
x *= 3 # multiplication
print(x)
x /= 3 # division
print(x)
x //= 3 # floor division i.e. returns an integer
print(x)
x %= 3 # returns remainder
print(x)
x **= 3 # returns the powered value
print(x)
x = 50
x |= 3 # OR operation
print(x)
x = 5
x &= 3 # AND
print(x)
x ^= 3 # XOR
print(x)
x <<= 3 # Left shift and assign i.e. Equivalent to integer multiplication by 2ⁿ
print(x)
x >>= 3 # Right shift and assign i.e. Equivalent to integer division by 2ⁿ
print(x)
print(x := 9) # assign and use value at the same line. super pythony code.


if (n := len("hello")) > 3:
    print(n)


numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")