#Functions
#Auyhor: Grace
#26-02-2024

#creat a function called say_hello
#its going to print hello
def say_hello():
    print("Hello!")



#creat a function called say_hello_params
#print "Hello {parameter}"
 #-----
    


    def say_Hello_params (name):
        print(f"Hello{name}!")


def how_big(num):
    if num < 0:
        return"very small"
    if num <10:
        return "pretty small"
    if num < 100:
        return"Big."
    if num < 1000:
        return "pretty big"




print(how_big(-1))

result = how_big(100_000_000)