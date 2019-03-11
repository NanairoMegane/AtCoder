# -*- coding: utf-8 -*-

# 入力された文字列
string = input()

# 最大処理数。100000以下なら文字列長。
max = min(len(string), 100000)

# 削除した文字数
del_count = 0

# 削除があった場合True
del_flg = True

# 削除文字がなくなるまでループする
while del_flg:
    del_flg = False

    # 
    for idx in range(max):
        if idx == max or idx > max:
            break
            
        # 照合対象の文字を切り出す
        target = string[idx : idx + 2]
        
        if target == "01" or target == "10":
            # 削除文字に一致した場合、元の文字列からそれを削除しカウントを進め、
            # 削除フラグを立てる
            string = string.replace(string[idx : idx + 2], '')
            print(string)
            del_count += 2
            max -= 2
            del_flg = True

print(del_count)
