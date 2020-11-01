#%%
import os, re
f_data = []
with open("biosSetup.txt", "r") as f:
    for line in f:
        f_data.append(line)
#%%
f_data[5:16]
#%%
with open("biosSetup.txt", "r") as f:
    print(f.tell())
#%%
for i, e in enumerate(f_data[5:16]):
    if '\n' ==  e:
        re.search('Fake Varstore Item', f_data[5:16][i+1])
        print(f_data[5:16][i+1], end = '')

#%%
def modify_values(kw):
    opt_pattern = r"Setup Question\s+=\s+{0}".format(kw['Setup Question'])
    kw = kw['Options']
    for i, e in enumerate(f_data[5:16]):
        ii = i
        if re.search(opt_pattern, e):
            # print(re.search(opt_pattern, e))
            for k in kw:
                while True:
                    ii += 1
                    line = f_data[5:16][ii]
                    if  re.match(k, line):
                        if k == 'Options':
                            re.sub(r'\d+', kw[k], line)
                            print(re.sub(r'\d+', kw[k], line))
                            # iii
                        else:
                            if re.search(r"\<", line):
                                re.sub(r'\<\d+\>', '<' + kw[k] + '>', line)
                                print(re.sub(r'\<\d+\>', '<' + kw[k] + '>', line))
                            elif re.search(r'\[', line):
                                re.sub(r'\[\d+\]', '[' + kw[k] + ']', line)
                                print(re.sub(r'\[\d+\]', '[' + kw[k] + ']', line))
                            else:
                                re.sub(r'\d+', kw[k], line)
                                print(re.sub(r'\d+', kw[k], line))
                        ii = i
                        break
                    if line == '\n':
                        ii = i
                        break
                ii = i
            break
#%%
Configure = {
    "Setup Question": 'Fake Varstore Item',
    "Options": {
        "Token": '%02%',
        "Width": "%02%",
        "Bios Default": "%02%"}
    }
modify_values(Configure)
#%%
import re
def demoReLookAheadBehind():
    inputStrList = [
        "date=20191224&name=CrifanLi&language=python",
        "language=python&name=CrifanLi&date=20191224", # lookahead will NOT match
        "language=python&name=CrifanLi date=20191224", # negative lookahead CAN match, the whole 'name=CrifanLi'
        "language=go&name=CrifanLi date=20191224", # positive lookbehind CAN match
        "language=go name=CrifanLi date=20191224", # negative lookbehind CAN match
    ]
    groupNormalPattern = "name=(\w+)" # 匹配任何 name=XXX 其中XXX是字母数字下划线均可
    groupLookaheadPattern = "name=(\w+)(?=&\w+)" # 只匹配后面 是&language 的情况
    groupNegativelookaheadPattern = "name=(\w+)(?!&)" # 只匹配后面 不是& 的情况
    groupPositivelookbehindPattern = "(?<=go&)name=(\w+)" # 只匹配前面 是go& 的情况
    groupNegativelookbehindPattern = "(?<!&)name=(\w+)" # 只匹配前面 不是& 的情况
    for curIdx, eachInputStr in enumerate(inputStrList):
        print("\n%s [%d] %s %s" % ("="*20, curIdx, eachInputStr, "="*20))
        foundGroupNormal = re.search(groupNormalPattern, eachInputStr)
        print("foundGroupNormal=%s" % foundGroupNormal)
#%%
demoReLookAheadBehind()
#%%
d = {'a': 1, 'b': 2}
d["a"]