#conditionals
# Grace Fan
15-02-2024

#implement the flowchart from notes
x = 1_000_000
y = -5.7

if x < y :
    print ("x is less than y")
if x > y :
    print ("x i sgreater than y")
if x == y :
    print ("x is equal to y")

if x < y :
    print ("x is less than y")
elif x > y :
    print ("x i sgreater than y")
else:
    print ("x is equal to y")

foo = int(input("Enter a number")) #string

if int(foo) < -1 or foo == 0:
    print("Foo is less than 1")
    print("or it's equal to zero")

#check if foo is inside a range
#greater tahn one and less than 1000
if foo > 1 and foo < 1000:
    print("foo is in the range 2-999")
else:
    print("foo is outside the range 2-999")

    
