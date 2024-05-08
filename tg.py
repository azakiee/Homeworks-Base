expected_user = 1000

User_by_day = [817, 1370, 752, 1247, 681, 1120, 915, 1281, 875, 1341, 757, 618, 812, 1170, 769, 1201, 845, 1289, 515,
               1247, 845, 1311, 741, 1239, 812, 638, 877, 1242, 1159, 1372.]
total = 0
max_users = 0
min_users = User_by_day[0]
for i in range(0, len(User_by_day)):

    if User_by_day[i] > max_users:
        max_users = User_by_day[i]
    elif User_by_day[i] > min_users:
        min_users = User_by_day[i]
    if User_by_day[i] < expected_user:
        print(i, expected_user - User_by_day[i])
    total = total + User_by_day[i]
    print(i, User_by_day[i], max_users, min_users)
average_user = total / len(User_by_day)

print(total / len(User_by_day))
print('Средняяя посещаемость', average_user)
print('Минимальное значение', min_users)
print('Максимальное значение', max_users)



