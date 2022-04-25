# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
def triangle():
    print("enter the lengths of the three sides of a triangle")
    prompta = int(input("a:"))
    promptb = int(input("b:"))
    promptc = int(input("c:"))
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
    if prompta == promptb == promptc:
        print(f"a triangle with sides of {prompta}, {promptb} & {promptc} is a equilateral triangle")
    elif prompta != promptb and promptb != promptc and promptc != prompta:
        print(f"a triangle with sides of {prompta}, {promptb} & {promptc} is a scalene triangle")
    elif prompta == promptb or prompta == promptc or promptb == promptc:
        print(f"a triangle with sides of {prompta}, {promptb} & {promptc} is a isosceles triangle")
# 3. Print a message such as:
#   - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
triangle()