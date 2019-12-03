import yagmail
import tools.common as com

def email():
	conf = com.jsonToDict("/config/account.conf")
    conf = conf['emial']

    email = yagmail.SMTP(host=conf['host'], user=conf['user'],
                    password=conf['password'])
    return email


def SMS():
    pass


if __name__ == '__main__':
    email = email()
    mail.send('test@163.com', subject='test tittle', contents='test content.')