#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Tested On Linux Operation System

# [
#   Developer: Sir Uidops
#   Email    : Sir.u1d0p5@gmail.com
#   Github   : https://github.com/siruidops/knowmail/
# ]

red    = "\033[0;31m"
green  = "\033[0;32m"
brown  = "\033[0;33m"
blue   = "\033[0;34m"
pur    = "\033[0;35m" 
tur    = "\033[0;36m"
yellow = "\033[1;33m"
end    = "\033[1;37m"

import sys
import os
from datetime import datetime
import subprocess
try:
	from validate_email import validate_email
except Exception as error:
	print
	print red+str(error)+' [Library: validate_email]'+end
	print
	sys.exit()
import getopt

logo = """
   __ __                __  ___     _ __
  / //_/__  ___ _    __/  |/  /__ _(_) /
 / ,< / _ \/ _ \ |/|/ / /|_/ / _ `/ / /
/_/|_/_//_/\___/__,__/_/  /_/\_,_/_/_/
"""

def single(email):
	is_valid = validate_email(email,verify=True)
	if str(is_valid).upper() == 'TRUE':
		print green+"    [+] Success: '{}' {}".format(email,end)
	else:
		print red+"    [-] NotFound: '{}' {}".format(email,end)
		

def fuel(file):
	try:
		f = open(file)
		emails = f.readlines()
		f.close()
	except:
		print
		print red+" Not Found Your Email File: {} {}".format(file, end)
		print
		sys.exit()
	for email in emails:
		email = email.strip()
		single(email)

def out(file, output):
	outputTotal = []
	try:
		f = open(file)
		emails = f.readlines()
		f.close()
	except:
		print
		print red+" Not Found Your Email File: {} {}".format(file, end)
		print
		sys.exit()
	for email in emails:
		email = email.strip()
		is_valid = validate_email(email,verify=True)
		if str(is_valid).upper() == 'TRUE':
			outputTotal.append(email)
		else:
			pass
	w = open(output, 'w')
	text = '\n'.join(outputTotal)
	w.write(text)
	w.close()
	print
	print green+" [+] Writed To '{}' {}".format(output,end)
	print

def banner():
	print
	print red+logo+end
	print
	print yellow+" Usage: ./knowmail.py [Options] [File/Email]"+end
	print
	print red+" Options:"+end
	print
	print brown+"   -e [opt/Email] "+end+':'+green+" Single Search Email"+end
	print brown+"   -f [opt/File]  "+end+':'+green+" File Search Email"+end
	print brown+"   -o [opt/File]  "+end+':'+green+" Write To Your Out Put File"+end
	print brown+"   -h             "+end+':'+green+" Show This Banner"+end
	print
	print red+" Example:"+end
	print
	print yellow+"   knowmail "+brown+'-e'+green+" sir.u1d0p5@gmail.com"+end
	print yellow+"   knowmail "+brown+'-f'+green+" email.txt"+end
	print yellow+"   knowmail "+brown+'-f'+green+" email.txt"+brown+" -o"+green+" out.txt"+end
	print yellow+"   knowmail "+brown+'-h'+end
	print
	sys.exit()

def main():
	fileI = False
	outI  = False
	argv  = sys.argv[1:]
	if len(sys.argv) == 1:
		banner()
	elif len(sys.argv) > 5:
		banner()
	else:
		pass
	try:
		opts,args = getopt.getopt(argv, '-e:-f:-o:-h')
	except:
		banner()
	for opt,arg in opts:
		if opt == '-e':
			fileI = False
			ev = arg
		elif opt == '-f':
			fileI = True
			f = arg
		elif opt == '-o':
			outI = True
			o = arg
		else:
			banner()
	if fileI == False:
		print
		print red+logo+end
		print
		single(ev)
		print
	elif fileI == True:
		if outI == True:
			print
			print red+logo+end
			print
			out(f,o)
			print
		else:
			print
			print red+logo+end
			print
			fuel(f)
			print
	else:
		pass

if __name__ == '__main__':
	main()
else:
	pass


