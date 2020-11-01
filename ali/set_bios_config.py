import re


# bios_config_file = 'biosSetup.txt'


def set_bios_config(option, attr, value, bios_config_file="biosSetup.txt", action="set_default"):
    with open(bios_config_file, 'r')as fp:
        content = fp.readlines()

    found = False
    modified = False
    opt_pattern = r"Setup Question\s+=\s+{0}".format(option)
    attr_pattern = r"{0}\s+=.+".format(attr)
    located = False
    for index, line in enumerate(content):
        if re.match(opt_pattern, line):
            found = True
            continue
        if not found:
            continue
        if line.strip() == "":
            break
        if attr != "Options":
            if re.match(attr_pattern, line):
                content[index] = re.sub(r"=((\[\w+\])?\w+)", lambda x: "=" + value if not x.group(2) else "=" + x.group(2) + value, line)
                modified = True
                break
        else:
            if located:
                if re.search(value, line):
                    content[index] = re.sub(r"(\*?\[\w+\]\w+)", lambda x: x.group(1) if x.group(1).startswith('*') else "*" + x.group(1), line)
                    modified = True
                else:
                    content[index] = re.sub(r"(\*?\[\w+\]\w+)", lambda x: x.group(1).lstrip("*"), line)
            elif re.match(attr_pattern, line):
                located = True
                if re.search(value, line):
                    content[index] = re.sub(r"(\*?\[\w+\]\w+)", lambda x: x.group(1) if x.group(1).startswith('*') else "*" + x.group(1), line)
                    modified = True
                else:
                    content[index] = re.sub(r"(\*?\[\w+\]\w+)", lambda x: x.group(1).lstrip("*"), line)

    print(''.join(content))
    if modified:
        return True
    return False


if __name__ == "__main__":
    flag = set_bios_config("Skip XML Compression", "BIOS Default", "Enable")
    print flag

