# Operator precedence describes the order in which operations are performed.

print((6 + 3) - (6 + 3)) # Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print(5 + 4 - 7 + 3) # Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right
print(100 + 5 * 3) # Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions

print("""
Operator	Description	
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
""")