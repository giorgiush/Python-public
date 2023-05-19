import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    var1 = input("0 - Rock\n1 - Paper\n2 - Scissors\n")
    if var1.isdigit():
        var1 = int(var1)
        if 0 <= var1 <= 2:
            list = [rock, paper, scissors]
            var2 = random.randint(0, 2)
            me = list[var1]
            cp = list[var2]

            print(f"YOU:\n{me}\n")
            print(f"Computer:\n{cp}\n")

            if me == cp:
                print("DRAW")
            elif (me == scissors and cp == rock) or (me == paper and cp == scissors) or (me == rock and cp == paper):
                print("YOU LOSE")
            else:
                print("YOU WIN")
        else:
            print("Invalid number")
    else:
        print("Invalid input, please enter a number.")
