import os
import sys
from robot.api import logger

filename = "./testdata/testdata.txt"

def main():
    if len(sys.argv)==1:
        logger.error("Error!!! Missing file data, sample: {}".format(filename))
    elif len(sys.argv) > 2:
        logger.error("Error!!! Unexpected values {}".format(sys.argv[2:]))
    else:
        sys.argv[1]
        x = get_log()
        print("_read_file_main() = {}".format(x))

def _read_file_std():
    try:
        f = open(filename, 'rt')
        for l in f.readline():
            print(l)
    finally:
        f.close()

def get_log():
    dict = {}
    with open(filename, 'r') as fr:
        data = fr.read()
    # x = eval(data)
    print(data)
    args = {k: v for (k, v) in data}
    print(args)


def cleanup(self, result_dir):
    files = os.listdir(os.getcwd())
    for file in files:
        if ".png" in file:
            shutil.move(file, result_dir)
        elif ".log" in file:
            shutil.move(file, result_dir)
        else:
            continue
    os.remove(qnxf)

def check_cansignal_log(self, exp=True, **kwargs):
    # return None
    b = self.get_log()
    logger.info("Get the log is [{0}]".format(b))
    s = re.compile("\s*(\S+),\s*Json\s*\:\s*\[(.*)\]", re.M | re.I)
    can_list = s.findall(b)
    ret = 0
    for key, value in kwargs.items():
        for i in can_list:
            tmp_can = json.loads(i[1])
            print(tmp_can)
            if (key.lower() == i[0].lower() or key.lower() == tmp_can.get("name").lower()) and str(
                    tmp_can.get("value")).lower() == str(value.lower()):
                ret = ret + 1
    tmp = ret >= len(kwargs.items())
    if tmp == exp:
        logger.info("We expect to check can signal {0} successful".format(kwargs.items()))
    else:
        # logger.error("We get the error can signal [{0}],and expect [{1}]".format(can_dict,kwargs.items()))
        raise Exception("We get the error can signal [{0}],and expect [{1}]".format(can_list, kwargs.items()))


if __name__ == "__main__":
    main()



