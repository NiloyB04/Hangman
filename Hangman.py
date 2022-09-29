import random

name = "HANGMAN"
divider = "---------------"
welcome = """             Welcome to my hangman game!    
            You will earn 10 points if you know a character
            and you will lose 5 points if your answer is wrong.
            If you give 5 wrong answers you will lose."""
print("\n{:^80}".format(name,))
print(welcome)
print("{:^80}".format(divider))

word = ["apple", "about", "above", "arise", "access", "account",
        "accountant", "beauty", "bell", "crow", "care", "clear", "dare",
        "demon", "dear", "dirty", "dragon", "enact", "easy", "empire", "eagle",
        "engine", "enough", "enquire", "fridge", "gate", "glare", "hello",
        "height", "igloo", "icicle", "island", "jelly", "jammed", "king", "kilogram"
        "kind", "leopard", "legend", "light", "mourn", "mustard", "murky", "natural",
        "named", "nickel", "onion", "oracle", "object", "pickel", "prison", "pineapple",
        "queen", "queer", "quack", "rollover", "roost", "radiate", "sunny", "silver",
        "sickly", "tired", "tamed", "teller", "union", "unicorn", "understood", "violin",
        "vehicle", "vehement", "wonder", "wallpaper", "willful", "xylophone", "yellow"
        "yeast", "yearn", "zebra", "zest", "zipper"]
choice = random.choice(word)
answer_characters = []
answer_characters.append("-" * len(choice))
solution = []
for i in answer_characters:
    for h in i:
        solution.append(h)
print("Word has {} letters.".format(len(choice)), ' '.join(solution))
print("" * 7)
lives = 5
points = 0
mistake1 = """  _________
  |
  |"""
mistake2 = "\n  O"
mistake3 = "\n \|/"
mistake4 = "\n  |"
mistake5 = "\n / \ "
hangman = ""
stored = ""
stored2 = ""
a = len(stored)
nonletter = "+/ 1234567890*-_?.,![{(]})"
while True:
    if len(stored) == len(choice):
        print("You win! Word: {} Your score: {}".format(choice, points))
        print("To quit press any button")
        break
    if lives == 0:
        print("\nYou lose...")
        print("Your score: {}".format(points))
        print("The answer was: {}".format(choice))
        print("To quit press any button")
        break
    x = input("\nPlease enter a letter: ")
    if 1 < len(x):
        print("\nEnter just one letter")
        continue
    if x in nonletter:
        print("\nYou have to enter a letter")
        continue
    if x in stored:
        print("You used this letter before!")
        continue
    if x in stored:
        print("You used this letter before!")
        continue
    if x in choice and not x in stored:
        points += 10 * choice.count(x)
        print("Letter {} is counted {} times.".format(x, choice.count(x)))
        for j, y in enumerate(choice):
            if 2 <= choice.count(y) and x == y:
                stored += x
                a += choice.count(y)
                if solution[j] == "-":
                    solution[j] = x
                print("In line {} .".format(j + 1))
            if choice.count(y) == 1 and x == y:
                stored += x
                a += choice.count(y)
                if solution[j] == "-":
                    solution[j] = x
                print("In line {} .".format(j + 1))
        print("\nWord:", ' '.join(solution))
    else:
        stored2 += x
        lives -= 1
        points -= 5
        print("\nThis letter {} not in our word! {} health left.".format(x, lives))
        print("\nWord:", ' '.join(solution))
        if lives == 4:
            hangman += str(mistake1)
            print(hangman)
        if lives == 3:
            hangman += str(mistake2)
            print(hangman)
        if lives == 2:
            hangman += str(mistake3)
            print(hangman)
        if lives == 1:
            hangman += str(mistake4)
            print(hangman)
        if lives == 0:
            hangman += str(mistake5)
            print(hangman)
try:
    input()
except SyntaxError:
    pass