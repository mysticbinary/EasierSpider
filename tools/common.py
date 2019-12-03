import re


def compareVersion(str1, str2):
    """
    对比version的版本号 返回大版本
    :param str1:
    :param str2:
    :return:
    """
    d1 = re.split('\.', str1)
    d2 = re.split('\.', str2)

    d1 = [int(d1[i]) for i in range(len(d1))]
    d2 = [int(d2[i]) for i in range(len(d2))]

    if (d1 > d2):
        return str1
    if (d1 < d2):
        return str2
    if (d1 == d2):
        return str1


def compareVersion_boole(str1, str2):
    """
    对比version的版本号 返回如果str1 > str2 返回True
    :param str1:
    :param str2:
    :return:
    """
    d1 = re.split('\.', str1)
    d2 = re.split('\.', str2)

    d1 = [int(d1[i]) for i in range(len(d1))]
    d2 = [int(d2[i]) for i in range(len(d2))]

    if (d1 > d2):
        return True
    if (d1 < d2):
        return False
    if (d1 == d2):
        return False




