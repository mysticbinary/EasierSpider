from urllib.request import quote


def enUrlcode(str):
    """
    str转url编码
    :param str:
    :return:
    """
    return quote(str)


def strTodict(str):
    """
    str转换成dict
    :param str:
    :return:
    """
    str = str.replace("null", "77777777")
    dicts = eval(str)
    return dicts


def strTodict2(str):
    """
    str转换成 dict
    :param str:
    :return:
    """
    s = str.split("&")

    dicts = {}
    for key in s:
        kv = key.split("=")
        dicts[kv[0]] = kv[1]
    return dicts


