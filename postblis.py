import requests
import sys
import urllib3
from colorama import Fore

urllib3.disable_warnings()

try:

	request_file = sys.argv[1]
	payloads_file = sys.argv[2]
	protocol = sys.argv[3]
	try:
		print('Detection in progress please be patient..\n')
		with open(request_file, 'r') as f:
			l = len(f.readlines())
			f.seek(0)
			x1 = f.readlines()[0].strip()
			f.seek(0)
			x2 = f.readlines()[l-1].strip()
			f.seek(0)
			x_dom = f.readlines()[1][6:].strip()
			# print(x_dom)
			f.seek(0)
			dict_head = dict()
			for t in range(2, l-2):
				chaka = f.readlines()[t].strip()
				# print(chaka.split(':'))
				f.seek(0)
				b1 = chaka.split(':')[0].strip()
				b2 = chaka.split(':')[1].strip()
				dict_head[b1] = b2
		# print(dict_head)
		the_path = x1[5:].replace(' HTTP/1.1', '')
		parent_url = protocol + '://' + x_dom + the_path
		dict_x = dict()
		with open(payloads_file, 'r') as f:
			for lines in f.readlines():
				if 'BHOOT' not in x2:
					print(Fore.RED + 'Unspecified injection point. Refer to the repo' + Fore.WHITE + '')
					sys.exit()
				else:

					part1, part2 = x2.split('BHOOT')
					final = part1 + lines.strip() + part2
					# print(final)
					x3 = final.split('&')
				
					for lol in x3:
						m1 = lol.split('=')[0]
						m2 = lol.split('=')[1]
						dict_x[m1] = m2
					
					resp = requests.post(parent_url, headers = dict_head, data = dict_x, verify = False, allow_redirects = True)

					if resp.elapsed.seconds >= 10:
						print(Fore.GREEN + '[Vulnerable]' + Fore.WHITE + ' ' +  Fore.BLUE + 'Detection Params: ' + str(dict_x) + Fore.WHITE + '')
					else:
						continue
	except KeyboardInterrupt:
		sys.exit()
except IndexError:
	print(Fore.RED + '[Usage]: ' + Fore.WHITE + 'python3 postblis.py <requestfile copy-paste from burp> <time-based-payloads> <http or https>' )
