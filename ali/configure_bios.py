#%%
import os, re
f_data = []
with open("biosSetup.txt", "r") as f:
    for line in f:
        f_data.append(line)
#%%
configure = {
    "Setup Question": 'Fake Varstore Item',
    "Options": {
        "Token": '%02%',
        "Width": "%02%",
        "BIOS Default": "%02%",
        "Value": "%02%",
        "Offset": "%02%"
        }
    }
#%%
def block_setupQuestion_options(setup_question):
    opt_pattern = r"Setup Question\s+=\s+{0}".format(setup_question)
    for file_index, file_element in enumerate(f_data):
        if re.search(opt_pattern, file_element):
            # print(file_index, f_data[file_index])
            for block_index, block_element in enumerate(f_data[file_index:]):
                if '\n' == block_element:
                    block_index = file_index + block_index
                    block_data = f_data[file_index: block_index]
                    return block_data, file_index, block_index
#%%
def modify_options(options, block_data):
    for option in options:
        for index, line in enumerate(block_data):
            if  re.match(option, line):
                        # Options	=[00]<1uS
                        if option == 'Options':
                            re.sub(r'\d+', options[option], line)
                            print(re.sub(r'\d+', options[option], line))
                            # iii
                        else:
                            # BIOS Default =[FF]Disable
                            # BIOS Default =[00]Disable
                            # BIOS Default =[00]+
                            # BIOS Default =[00]-6.0 dB
                            # BIOS Default =[00]40-50ms(spec 50us-50ms)
                            if re.search(r"\[\w+\]\S+", line):
                                block_data[index] = re.sub(r"(?<=\]).+", options[option], line)
                            # BIOS Default =[00]
                            elif re.search(r"\[\w+\]", line):
                                block_data[index] = re.sub(r"(?<=\[)\w+(?=\])", options[option], line)
                            # BIOS Default =<1000>
                            elif re.search(r'<\d+>', line):
                                block_data[index] = re.sub(r"(?<=\<)\w+(?=\>)", options[option], line)
                            # Value	="1111:2222:3333:4444:5555:6666:7777:8888"
                            elif re.search(r'".*"', line):
                                block_data[index] = re.sub(r"(?<=\").*(?=\")", options[option], line)
                            # BIOS Default =1
                            # BIOS Default =3F
                            else:
                                block_data[index] = re.sub(r"(?<==)\w+", options[option], line)
    return block_data
#%%
def configure_bios(configure):
    setup_question = configure["Setup Question"]
    block_data, block_start, block_end = block_setupQuestion_options(setup_question)
    options = configure['Options']
    f_data[block_start: block_end] = modify_options(options, block_data)
    return f_data[block_start: block_end]
#%%
configure_bios(configure)
#%%
