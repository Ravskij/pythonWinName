count_human = int(input())
name_and_result = []
win_list = []
for i in range(count_human):
    now_word = input()
    name_and_result.append(now_word.split(" "))
for j in name_and_result:
    for k in j:
        if k == "win":
            win_list.append(j)
win_names = [x[0] for x in win_list]
print(win_names)
print(len(win_names))