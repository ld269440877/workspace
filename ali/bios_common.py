import subprocess
import re


def parse_bios_opt(bios_config_file="biosSetup.txt"):
    with open(bios_config_file, "r")as fh:
        content = fh.read()
    content = [line for line in content.split('\n\n') if line.startswith("Setup")]

    configs = dict()
    for config in content:
        lines = config.splitlines()
        bios_cfg = lines[0].split("=")[-1].strip()
        configs[bios_cfg] = {"Options": []}
        k = None
        for line in lines[1:]:
            line = line.split("=")
            if len(line) == 2:
                k = line[0].strip()
            if k is None:
                return False, "parse config({0}) failed !".format(config)
            value = line[-1].split("//")[0].strip()
            if k == "Options":
                configs[bios_cfg][k].append(value)
            else:
                configs[bios_cfg][k] = value

    return True, configs


def compare_opt(configs, option, attr, condition, expect):
    def check_has(x, y):
        if isinstance(x, str):
            x = [x]
        for i in x:
            if y in i:
                return True

        return False

    def check_default(x, y):
        if isinstance(x, str):
            x = [x]
        pattern = r"\*\[\w+\]" + y
        for i in x:
            matched = re.match(pattern, i)
            if matched:
                return True
        return False

    compare_func = {
        '=': lambda x, y: (float(x) == float(y)),
        'eq': lambda x, y: (str(x) == str(y)),
        'has': lambda x, y: check_has(x, y),
        "is_default": lambda x, y: check_default(x, y)
    }
    return compare_func[condition](configs[option][attr], expect)


def get_bios_config_file(bios_config_file="biosSetup.txt"):
    cmd = "/tmp/tools/bios/SCELNX_64 /o /s {0}".format(bios_config_file)
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = ret.stdout.read().strip()
    error = ret.stderr.read().strip()
    if error:
        if "successfully" in (output + error):
            return True, output
        print("[%s] execute FAIL !Error:%s" % (cmd, error))
        return False, error
    return True, output


def execute(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    output = output.decode('utf8')
    error = error.decode('utf8')
    if error:
        return False, error
    return True, output


def compose_ipmi_cmd(ipmi_host="127.0.0.1", ipmi_user="admin", ipmi_passwd="admin", ipmi_port="623", interface="lan", local=False, tail_cmd=""):
    if local:
        return "ipmitool " + tail_cmd
    else:
        return "ipmitool -H {0} -U {1} -P {2} -p {3} -I {4} {5}".format(ipmi_host, ipmi_user, ipmi_passwd, ipmi_port,
                                                                        interface, tail_cmd)


def set_bios_config(option, attr, value, bios_config_file="biosSetup.txt"):
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
    if modified:
        return True, content
    return False, content
