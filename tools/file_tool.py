import hashlib
import os.path
import os
import getRootPath
import shutil


def fileMd5(filepath):
    """
    获取文件MD5码
    :param filepath:
    :return:
    """
    if os.path.isfile(filepath):
        fp = open(filepath, 'rb')
        contents = fp.read()
        fp.close()
        filemd5str = hashlib.md5(contents).hexdigest()
        return filemd5str
    else:
        print('file not exists.')


def fileSize(filepath):
    """
    获取文件size
    :param filepath:
    :return:
    """
    return os.path.getsize(filepath)


def is_suitablesize(apkname):
    """
    判断文件是否是正常apk文件
    :param apkname:
    :return:
    """
    path = getRootPath.getRootPath() + "/download/"
    apksize = os.path.getsize(path + apkname + ".apk")
    if apksize >= 10000:
        return True
    else:
        return False

def fileDownload(url,filename):
    """
    文件下载
    :param apkname:
    :param url:
    :return:
    """
    # 下载前先清空 /download
    path = getRootPath.getRootPath() + "/download/"

    # 删除文件夹
    if os.path.exists(path):
        shutil.rmtree(path)

    # 创建文件夹
    if not os.path.exists(path):
        os.mkdir(path)

    # 把下载地址发送给requests模块
    f = requests.get(url)

    # 下载文件
    filename = getRootPath.getRootPath() + "/download/" + filename
    with open(filename, "wb") as code:
        code.write(f.content)
