import getRootPath
import json


def writerjson(path, data):
    """
    将dict写入文本，w+ 直接把原来的文本覆盖
    :return:
    """
    with open(getRootPath.getRootPath() + path, "w+", encoding="utf8") as f:
        json.dump(data, f)


def readjson(path):
    """
    读json
    :return:
    """
    with open(getRootPath.getRootPath() + path, "r", encoding="utf8") as f:
        allproduct_list = json.loads(f.read())
    return allproduct_list


def getAccount(name):
    """
    获取账号信息
    :param name:
    :return:
    """
    accountdict = readjson("/config/account.conf")
    account = accountdict[name]
    return [account["account"], account["password"]]


def jsonToDict(pathstr):
    """
    json转换dict
    :param pathstr:
    :return:
    """
    rootPath = getRootPath.getRootPath()
    confpath = rootPath + pathstr

    with open(confpath, 'r', encoding="utf8") as confFile:
        confStr = confFile.read()

    conf = json.JSONDecoder().decode(confStr)
    return conf