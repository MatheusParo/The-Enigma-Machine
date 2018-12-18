letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
one ="YRUHQSLDPXNGOKMIEBFZCWVJAT"

def setup():
    print("wiring = [",end="")
    for i in range(len(letters)):
        print("["+str(i)+", "+str(one.index(letters[i]))+"], ",end="")
    print("]")


def right():
    stupid = ["z","z","", "z","z","z", "", "a", ""]
    first = ""
    second = ""
    for i in range(1,len(stupid),2):
        if stupid[i] and stupid[i-1]:
           print(stupid[i-1], stupid[i])
        else:
            continue
def lazy():
    for i in range(20):
        print("letter%s.text, "%(i),end="")
lazy()