import random

def soccer():
    goalie = [r"""
                  ---------------------
                  |                    |
                  |                    |
                  |                    |
                  |         0          |
                  |        /|\         |
                  |        / \         | """]
    
    o1 = [r"""
              --------------------- 
              | O                  |
              | \\0                |
              |    \               |
              |    \ \             |
              |                    |
              |                    | """]

    o2 = [r"""
              ---------------------
              | O      \0/         | 
              |         |          | 
              |        / \         | 
              |                    | 
              |                    | 
              |                    | """]
    o3 = [r"""
              --------------------- 
              | O                  | 
              |                0// | 
              |               /    | 
              |             / /    | 
              |                    | 
              |                    | """]
    o4 = [r"""
              --------------------- 
              | O                  |
              |                    |
              |                    |
              |                    |
              | \\0                |
              |    \ //            | """]
    o5 = [r"""
              ---------------------
              | O                  |
              |                    |
              |                    |
              |         0          |
              |        /|\         |
              |        / \         | """]
    o6 = [r"""
              --------------------- 
              | O                  | 
              |                    | 
              |                    | 
              |                    | 
              |                0// | 
              |            \\ /    | """]

    two1 = [r"""
                ---------------------
                |          O         | 
                | \\0                | 
                |    \               | 
                |    \ \             | 
                |                    | 
                |                    | """]

    two2 = [r"""
                --------------------- 
                |        \0/         | 
                |         O          | 
                |        / \         | 
                |                    | 
                |                    | 
                |                    | """]
    two3 = [r"""
                --------------------- 
                |          O         | 
                |                0// | 
                |               /    | 
                |             / /    | 
                |                    | 
                |                    | """]
    two4 = [r"""
                --------------------- 
                |          O         | 
                |                    | 
                |                    |
                |                    | 
                | \\0                | 
                |    \ //            | """]
    two5 = [r"""
                --------------------- 
                |          O         | 
                |                    | 
                |                    | 
                |         0          | 
                |        /|\         | 
                |        / \         | """]
    two6 = [r"""
                --------------------- 
                |          O         | 
                |                    | 
                |                    | 
                |                    | 
                |                0// | 
                |            \\ /    | """]

    three1 = [r"""
                --------------------- 
                |                  O | 
                | \\0                | 
                |    \               | 
                |    \ \             | 
                |                    | 
                |                    | """]

    three2 = [r"""
                --------------------- 
                |        \0/       O | 
                |         |          | 
                |        / \         | 
                |                    | 
                |                    | 
                |                    | """]
    three3 = [r"""
                --------------------- 
                |                  O | 
                |                0// | 
                |               /    | 
                |             / /    | 
                |                    | 
                |                    | """]
    three4 = [r"""
                --------------------- 
                |                  O | 
                |                    | 
                |                    | 
                |                    |
                | \\0                | 
                |    \ //            | """]
    three5 = [r"""
                --------------------- 
                |                  O | 
                |                    | 
                |                    | 
                |         0          | 
                |        /|\         | 
                |        / \         | """]
    three6 = [r"""
                --------------------- 
                |                  O |
                |                    | 
                |                    | 
                |                    | 
                |                0// | 
                |            \\ /    | """]
    four1 = [r"""
                ---------------------
                |                    |
                | \\0                | 
                |    \               | 
                |    \ \             | 
                | O                  | 
                |                    | """]

    four2 = [r"""
                ---------------------
                |        \0/         | 
                |         |          | 
                |        / \         | 
                |                    | 
                | O                  | 
                |                    | """]
    four3 = [r"""
                --------------------- 
                |                    | 
                |                0// | 
                |               /    | 
                |             / /    | 
                | O                  | 
                |                    | """]
    four4 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |                    | 
                | O\\0               | 
                |    \ //            | """]
    
    four5 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |         0          | 
                | O      /|\         | 
                |        / \         | """]
    four6 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |                    | 
                | O              0// | 
                |            \\ /    | """]

    five1 = [r"""
                --------------------- 
                |                    | 
                | \\0                | 
                |    \               | 
                |    \ \             | 
                |                    | 
                |          O         | """]

    five2 = [r"""
                --------------------- 
                |        \0/         | 
                |         |          | 
                |        / \         | 
                |                    | 
                |                    | 
                |          O         | """]
    five3 = [r"""
                --------------------- 
                |                    | 
                |                0// | 
                |               /    | 
                |             / /    | 
                |                    | 
                |          O         | """]
    five4 = [r""" --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |                    |
                | \\0                | 
                |    \ //  O         | """]
    five5 = [r"""
                 --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |         0          | 
                |        /|\         | 
                |        / O         | """]
    five6 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |                    | 
                |                0// | 
                |          O \\ /    | """]

    six1 = [r"""
                --------------------- 
                |                    | 
                | \\0                | 
                |    \               | 
                |    \ \             | 
                |                  O | 
                |                    | """]

    six2 = [r"""
                --------------------- 
                |        \0/         | 
                |         |          | 
                |        / \         | 
                |                    | 
                |                  O | 
                |                    | """]
    six3 = [r"""
                --------------------- 
                |                    | 
                |                0// | 
                |               /    | 
                |             / /    | 
                |                  O | 
                |                    | """]
    six4 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |                    | 
                | \\0              O | 
                |    \ //            | """]
    six5 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |         0          | 
                |        /|\       O | 
                |        / \         | """]
    six6 = [r"""
                --------------------- 
                |                    | 
                |                    | 
                |                    | 
                |                    | 
                |               0//O | 
                |            \\ /    | """]
    
    while True:
        q = input('How many goals do you want to play? \n')
        if q == '' or not q in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print('Please put a number between 1 and 10. \n')
        else:
           shots = int(q)
           break
                
    score = ["_"] * shots
    for i in goalie:
        print(i)
    for i in range(0, shots):
        print("\n SCORE: {} \n".format(' '.join(score)))
        print('''   Where do you want to put the ball?

                    TOPL    TOPM    TOPR
                    BTML    BTMM    BTMR''')
        cpt = random.randint(1,6)
        while True:
            answer = input().lower()
            if answer == 'topl':
                if cpt == 1:
                    for i in o1:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("X")
                    print("what a save!")
                    break
                if cpt == 2:
                    for i in o2:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 3:
                    for i in o3:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 4:
                    for i in o4:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 5:
                    for i in o5:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 6:
                    for i in o6:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break

            if answer == 'topm':
                if cpt == 1:
                    for i in two1:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 2:
                    for i in two2:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("X")
                    print("what a save!")
                    break
                if cpt == 3:
                    for i in two3:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 4:
                    for i in two4:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 5:
                    for i in two5:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 6:
                    for i in two6:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break

            if answer == 'topr':
                if cpt == 1:
                    for i in three1:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 2:
                    for i in three2:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 3:
                    for i in three3:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("X")
                    print("what a save!")
                    break
                if cpt == 4:
                    for i in three4:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 5:
                    for i in three5:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 6:
                    for i in three6:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break

            if answer == 'btml':
                if cpt == 1:
                    for i in four1:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 2:
                    for i in four2:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 3:
                    for i in four3:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 4:
                    for i in four4:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("X")
                    print("What a save!")
                    break
                if cpt == 5:
                    for i in four5:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 6:
                    for i in four6:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break

            if answer == 'btmm':
                if cpt == 1:
                    for i in five1:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 2:
                    for i in five2:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 3:
                    for i in five3:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 4:
                    for i in five4:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 5:
                    for i in five5:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("X")
                    print("what a save!")
                    break
                if cpt == 6:
                    for i in five6:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
            if answer == 'btmr':
                if cpt == 1:
                    for i in six1:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 2:
                    for i in six2:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 3:
                    for i in six3:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 4:
                    for i in six4:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!!")
                    break
                if cpt == 5:
                    for i in six5:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("O")
                    print("GOAL!!!")
                    break
                if cpt == 6:
                    for i in six6:
                        print(i)
                    if score[0] == "_":
                        del score[0]
                        score.append("X")
                    print("what a save!")
                    break
            else:
                answer = input('''   Where do you want to put the ball?
                                        1. TOPL
                                        2. TOPM
                                        3. TOPR
                                        4. BTML
                                        5. BTMM
                                        6. BTMR''')
    
    tgoals = score.count('O')
    tmisses = score.count('X')
    if tgoals > tmisses:
        print("You have won text soccer with {} goals and {} misses!".format(tgoals, tmisses))
    else:
        print("You have lost text soccer with {} goals and {} misses.".format(tgoals, tmisses))

soccer()
