"""
Session 2:
1) Conditional Statement
2) Loopimg Statement
"""

#if statement
'''
if <condition>:
   <statement_1>
   <statement_2>
'''

'''
-------------To Find Smallest number in all possible combinations
'''
"""
number_01 = 51
number_02 = 51
number_03 = 500
if number_01 == number_02 == number_03:
    print("All are same")
elif number_01 == number_02 < number_03:
    print("number_01 and number_02 are minimum")
elif number_01 == number_03 < number_02:
    print("number_01 and number_03 are minimum")
elif number_01 < number_02 <= number_03:
    print("number_01 is smallest")
elif number_02 == number_03 < number_01:
    print("number_02 and number_03 are minimum")
elif number_02 < number_01 and number_02 < number_03:
    print("number_02 is smallest")
elif number_03 < number_01 and number_03 < number_02:
    print("number_03 is smallest")
    
"""
"""
---------------------Fibonnaci ------------------------------
"""
"""

a = 0
b = 1
print(a , b)
for i in range(1, 10):
    res = a+b
    a = b
    b = res
    print(res)

"""

"""
----------To find Prime Number between 1 to 20
"""


for i in range (2, 20):
    counter = 0
    for j in range(2, 9):
        if i % j == 0:
            break
        else:

            print(i)






