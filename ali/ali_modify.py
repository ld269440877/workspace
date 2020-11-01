#%%
import os, re
f_data = []
with open("biosSetup.txt", "r") as f:
    for line in f:
        f_data.append(line)
#%%
# f_data[54620: 54640]
#%%
#
#
# test data
#
#
f_data= ['HIICrc32= A0E51F1B\n',
 '\n',
 'Setup Question\t= Fake Varstore Item\n',
 'Token\t=<01>\t// Do NOT change this line\n',
'Offset\t=[00]\n'
 'Width\t=01\n',
 'BIOS Default =[00]Disable \n',
 'Options\t=*[00]Disable\t// Move "*" to the desired Option\n',
 '         [01]Disable\n',
 'Value\t="1111:2222:3333:4444:5555:6666:7777:8888"',
 
 '\n',
 'Setup Question\t= C002d\n']
#%%
def modify_values(kw):
    opt_pattern = r"Setup Question\s+=\s+{0}".format(kw['Setup Question'])
    kw = kw['Options']
    for i, e in enumerate(f_data):
        ii = i
        if re.search(opt_pattern, e):
            # print(re.search(opt_pattern, e))
            for k in kw:
                while True:
                    ii += 1
                    line = f_data[ii]
                    if  re.match(k, line):
                        # Options	=[00]<1uS
                        if k == 'Options':
                            re.sub(r'\d+', kw[k], line)
                            print(re.sub(r'\d+', kw[k], line))
                            # iii
                        else:
                            # BIOS Default =[FF]Disable
                            # BIOS Default =[00]Disable
                            # BIOS Default =[00]+
                            # BIOS Default =[00]-6.0 dB
                            # BIOS Default =[00]40-50ms(spec 50us-50ms)
                            if re.search(r"\[\w+\]\S+", line):
                                re.sub(r"(?<=\]).+", kw[k], line)
                                print(re.sub(r"(?<=\])\w+", kw[k], line))
                            # BIOS Default =[00]
                            elif re.search(r"\[\w+\]", line):
                                re.sub(r"(?<=\[)\w+(?=\])", kw[k], line)
                                print(re.sub(r"(?<=\[)\w+(?=\])", kw[k], line))
                            # BIOS Default =<1000>
                            elif re.search(r'<\d+>', line):
                                re.sub(r"(?<=\<)\w+(?=\>)", kw[k], line)
                                print(re.sub(r"(?<=\<)\w+(?=\>)", kw[k], line))
                            # Value	="1111:2222:3333:4444:5555:6666:7777:8888"
                            elif re.search(r'".*"', line):
                                re.sub(r"(?<=\").*(?=\")", kw[k], line)
                                print(re.sub(r"(?<=\").*(?=\")", kw[k], line))
                            # BIOS Default =1
                            # BIOS Default =3F
                            else:
                                re.sub(r"(?<=\=)\w+", kw[k], line)
                                print(re.sub(r"(?<=\=)\w+", kw[k], line))
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
        "BIOS Default": "%02%",
        "Value": "%02%",
        "Offset": "%02%"
        }
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
re.search(r"(?<=\<)\w+(?=\>)", 'BIOS Default =<00> ')

#%%
re.sub(r"(?<=\[)\w+(?=\])", '%02%', '[00]')
#%%
'Offset\t=[A30]'
re.sub(r"\[\w+\]", '%02%', '[A30]')
