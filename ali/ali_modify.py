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
def modify_values(setup_question, **kw):
    kw["BIOS Default"] = kw.pop("Bios_Default")
    opt_pattern = r"Setup Question\s+=\s+{0}".format(setup_question)
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
                            re.sub('\d+', kw[k], line)
                            print(re.sub('\d+', kw[k], line))
                            # iii 
                        else:
                            if re.search(r"\<", line):
                                re.sub('\<\d+\>', '<' + kw[k] + '>', line)
                                print(re.sub('\<\d+\>', '<' + kw[k] + '>', line))
                            elif re.search(r'\[', line):
                                re.sub('\[\d+\]', '[' + kw[k] + ']', line)
                                print(re.sub('\[\d+\]', '[' + kw[k] + ']', line))
                            else:
                                re.sub('\d+', kw[k], line)
                                print(re.sub('\d+', kw[k], line))
                        ii = i
                        break             
                    
                    if line == '\n':
                        ii = i
                        break
                ii = i
            break
#%%
modify_values('Fake Varstore Item', Token = '02', Width = '02', Bios_Default = '02')     

