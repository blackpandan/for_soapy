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
                    choices2 = choice + "," + " "
                    print(choices2)    
                choosed = input("\nInput Choice: ")
                if choosed == "blue" or choosed == "Blue" or choosed == "BLUE":
                    total_poll += 1
                    blue += 1
                elif choosed == "red" or choosed == "Red" or choosed == "RED":
                    total_poll += 1
                    red += 1
                elif choosed == "green" or choosed == "Green" or choosed == "GREEN":
                    total_poll += 1
                    green += 1
                else:
                    print("wrong input")
                print("\n")
                print("blue: " + str(blue) + " votes")
                print("red: " + str(red) + " votes")
                print("green: " + str(green) + " votes")
                print("\n")
                sleep(5)
                clear()
    def add(choice):
        polls.choices.append(choice)
    def rem(choice):
        polls.choices.remove(choice)
    def avail():
        print(polls.choices)


