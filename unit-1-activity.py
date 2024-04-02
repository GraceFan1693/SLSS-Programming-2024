#Unite Activity
#Grace Fan
##04-3-2024

print("Hello,I'm Grace , What's you name?")
name = input()

print(f"it's nice to meet you! {name}")

outside= input ("would you like to go outside with me?(Yes/No)")

outside = outside.strip()
if outside.lower()=="no":
     answer=input("Looking forward to our next meeting")
     
if outside.lower()=="yes":
   answer=input("Ok ,so what time can we meet?(morning/afternoon)")

if answer == "morning"or"Morning":
      print("ok,see you later")

else :
     print("see you this afternoon")


