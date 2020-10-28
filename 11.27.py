#Yasir Mushtaque
#1769403

team_dict = {}
for x in range(1, 6):
    j_num = int(input("Enter player {}'s jersey number:\n".format(x)))
    rating = int(input("Enter player {}'s rating:\n".format(x)))
    print()
    if j_num > 99 and j_num < 0 and rating > 9 and rating < 0:
        break
    else:
        team_dict[j_num] = rating

keys = list(team_dict.keys())
keys.sort()
print('ROSTER')
for x in keys:
    print("Jersey number: %d, Rating: %d" % (x, team_dict[x]))

menu = ''
while menu != 'q':
    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')

    menu = input('Choose an option:\n')
    if menu == 'a':
        j_num = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        team_dict[j_num] = rating

    elif menu == 'd':
        j_num = int(input("Enter a jersey number:\n"))
        if j_num in team_dict.keys():
            del team_dict[j_num]

    elif menu == 'u':
        j_num = int(input("Enter a jersey number:\n"))
        if j_num in team_dict.keys():
            rating = int(input("Enter a new rating for player:\n"))
            team_dict[j_num] = rating

    elif menu == 'r':
        rating_parameter = int(input("Enter a rating:\n"))
        print('ABOVE', rating_parameter)
        for j_num, rating in sorted(team_dict.items()):
            if rating > rating_parameter:
                print("Jersey number: %d, Rating: %d" % (j_num, rating))

    elif menu == 'o':
        print("ROSTER")
        for j_num, rating in sorted(team_dict.items()):
            print("Jersey number: %d, Rating: %d" % (j_num, rating))