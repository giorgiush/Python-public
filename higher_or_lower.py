data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

import random
a = random.choice(data)
score = 0
def presentation(A, B):
    print(f'SCORE: {score}\nWho has more followers?\nA: {A["name"]}, a {A["description"]}, from {A["country"]}\nB: {B["name"]}, a {B["description"]}, from {B["country"]}')

def check(answer, other):
    global a
    global score
    if answer["follower_count"] > other["follower_count"]:
        score += 1
        a = answer
    else:
        return 0
def game():
    global a
    b = random.choice(data)
    while b == a:
        b = random.choice(data)
    presentation(a, b)
    answer = input("Enter 'A' or 'B': ").lower()
    if answer == "a":
        if check(answer=a, other=b) == 0:
            print(f"Wrong. Your final score is {score}")
        else:
            game()
    else:
        if check(answer=b, other=a) == 0:
            print(f"Wrong. Your final score is {score}")
        else:
            game()
game()
