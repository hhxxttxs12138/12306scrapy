import requests
import re
from pprint import pprint

def st():
	url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9048"
	r = requests.get(url)
	pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
	station_name = re.findall(pattern,r.text)
	pprint(dict(station_name), indent = 4)

if __name__ == '__main__':
	st()
