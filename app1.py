import requests
import tools.log as log

def main():
    logs = log.get_logger()
    logs.info("-================Start.================-")
    result = requests.get(url="https://api.github.com/")
    logs.debug(result.text)
    logs.info("-================End.================-")


if __name__ == '__main__':
    main()