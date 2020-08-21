from os import system, name
from time import sleep
def clear():
	if name == "nt":
		_= system("cls")
	else:
		 _= system("clear")

class polls:
    question = "\nwhich color do u prefer: \n"
    choices = ["red", "blue", "green"]


    def __init__(self, ac):
        self.ac = ac

    def req(self):
        if self == "start":
            total_poll = 0
            blue = 0
            red = 0
            green = 0
            while total_poll < 20:
                print("\n")
                print(polls.question)
                for choice in polls.choices:
                    choices2 = f"{choice}, "
                    print(choices2)    
                choosed = input("\nInput Choice: ")
                if choosed.lower == "blue":
                    total_poll += 1
                    blue += 1
                elif choosed.lower == "red":
                    total_poll += 1
                    red += 1
                elif choosed.lower == "green":
                    total_poll += 1
                    green += 1
                else:
                    print("wrong input")
                print("\n")
                print(f"blue: {blue}votes✓")
                print("red: {red} votes✓")
                print("green: {green}votes✓")
                print("\n")
                sleep(5)
                clear()
    def add(choice):
        polls.choices.append(choice)
    def rem(choice):
        polls.choices.remove(choice)
    def avail():
        print(polls.choices)


