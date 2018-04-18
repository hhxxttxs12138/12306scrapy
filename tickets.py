#*- coding: utf-8 -*- #
"""Tickets System

Usage:
  tickets [-dgkzt] <from> <to> <date>

Options:
  -h --help     Show this screen.
  -d            动车
  -g            高铁
  -k            快速
  -z            直达
  -t            特快

  """
import requests
import colorama
from docopt import docopt
from stations import Stations
import stations
from prettytable import PrettyTable
from colorama import Fore

def cli():

	arguments = docopt(__doc__, version='Tickets System 1.0')
	from_station = Stations.get(arguments.get('<from>'), None)
	to_station = Stations.get(arguments.get('<to>'), None)
	date = arguments.get('<date>')

	url = '''https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'''.format(date, from_station, to_station)
	r = requests.get(url)
	raw_trains = r.json()['data']['result']
	pt = PrettyTable(["车次", "车站", "时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "硬卧", "软座", "硬座", "无座"])
	pt.align["车次"] = "l"
	for raw_train in raw_trains:
		data_list = raw_train.split('|')
		train_no = data_list[3]
		start_station = stations.get_station(data_list[6])
		end_station = stations.get_station(data_list[7])
		start_time = data_list[8]
		arrive_time = data_list[9]
		lishi = data_list[10]
		swz_num = data_list[32]
		ydz_num = data_list[31]
		edz_num = data_list[30]
		gjrw_num = data_list[21]
		tdz_num = data_list[25]
		rw_num = data_list[23]
		dw_num = data_list[27]
		yw_num = data_list[28]
		rz_num = data_list[24]
		yz_num = data_list[29]
		wz_num = data_list[26]
		qt_num = data_list[22]

		pt.add_row([
			train_no,
			'\n'.join((Fore.GREEN + start_station + Fore.RESET, Fore.RED + end_station + Fore.RESET)),
			'\n'.join((Fore.GREEN + start_time + Fore.RESET, Fore.RED + arrive_time + Fore.RESET)),
			lishi,
			swz_num,
			ydz_num,
			edz_num,
			gjrw_num,
			rw_num,
			yw_num,
			rz_num,
			yz_num,
			wz_num])

	colorama.init()
	print(pt)

if __name__ == '__main__':
	cli()
