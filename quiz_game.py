print("wellcome to my computer quiz")

playing=input("do you want to play ? ")
if playing != "yes":
    quit()
print("okey let play : ")
answer= input ("what does CPU stand for ??")
print("correct") if answer == "central processing unit" else print("false")