list = [0, 1, 1, 0, 0, 0, 1]
new_list = []
# デフォルト
tmp = list[0]

# 六回の比較を行います
for num in range(len(list) - 1):
    # 同じの場合、加算させます
    if list[num] == list[num + 1]:
        tmp += list[num+1]
        # 最後の比較で同じだった場合、加算させた値をappendする
        if num == len(list) - 2:
            new_list.append(tmp)
    # 違った場合、appendします
    else:
        new_list.append(tmp)
        # 最後の比較で違った場合、listの最後の値をappendする
        if num != len(list) - 2:
            tmp = list[num + 1]
        else:
            new_list.append(list[len(list) - 1])

# new_listをprintする
print(new_list)