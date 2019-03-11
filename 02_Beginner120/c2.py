# -*- coding: utf-8 -*-
import re
# 入力された文字列
string = input()

raw_length = len(string)

# 削除があった場合True
del_flg = True

# 削除文字がなくなるまでループする
while del_flg and len(string) != 0:
    del_flg = False
    before_length = len(string)
    string = re.sub('01|10', '', string)
    after_length = len(string)
    
    if before_length != after_length:
        del_flg = True

print((raw_length - len(string)))