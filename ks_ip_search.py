import urllib.request
from threading import Thread
import requests
from time import time 
# from bs4 import BeautifulSoup
# import subprocess 
# import socketserver
import socket
# import os
# from time import sleep
# from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor

htmltxt=""
htmltext=""

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return str(IP)
    

#cmd="python iptesting.py"
#output = check_output(cmd, stderr=STDOUT, timeout=5)
#print (output)

#ip=subprocess.Popen(["python", "iptesting.py"], stdout=subprocess.PIPE)
#sleep(3)
#try:
#	urllib.request.urlopen("http://127.0.0.1:5020/stop")
#except:
#	out, err = ip.communicate()
#	print ("out ",out)
#	print ("error ")

#print ("Ip ",ip)

#extip=extract_ip()
#ipl=extip.split('.')[:-1]
#extip=".".join(ipl)+"."

#import socket 

##
##st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##try:       
##    st.connect(('10.255.255.255', 1))
##    IP = st.getsockname()[0]
##except Exception:
##    IP = '127.0.0.1'
##finally:
##    st.close()
##print (str(IP))
##extip=".".join(IP.split(".")[:-1])+"."

ips=[]
def reqip(ip):
    try:
        html = requests.request('HEAD',ip,timeout=1, verify=False)
        if html:
            print('Text: ',html.text)
            ips.append(ip)
            #print('Ip Found: ', ip)
    except:
        #print (ip+" nothing found")
        pass

def checkip(ip):
	try:
		html=urllib.request.urlopen(ip)
		if html:
			ips.append(ip)
##			htmltext=urllib.request.Request(ip)
			print (ip+" ip found")
	except:
			print (ip+" nothing found")

#st=time()		
#for i in range (1,256):
#	ip="http://192.168.43."+str(i)+":8080"
#	thread=Thread(target=checkip,args=(ip,))
#	thread.start()
#		
#thread.join()
#en=time()
#print (f"cip time: {en-st}")

def get_ips():
    ips.clear()
    IP=extract_ip()
    extip=".".join(IP.split(".")[:-1])+"."
    print(extip)

    ##sta=time()
    ip_list=[]
    for i in range(1,256):
        ip="http://"+extip+str(i)+":8080"
        ip_list.append(ip)
    
        # thread=Thread(target=reqip,args=(ip,))
        # thread.start()
    with ThreadPoolExecutor(max_workers=255) as executor:
        executor.map(reqip,ip_list)
    
    return ips

if __name__=='__main__':
    print(get_ips())
	
##end=time()
##print (f"rip time: {end-sta}")
##htmltxt=htmllist[0].text
##print (htmltxt,len(htmltxt))
#print (htmltext,len(htmltext))


##soup = BeautifulSoup(htmltxt, "html.parser")
##print (soup)
##links=soup.select("a")
##actual_web_links = [web_link['href'] for web_link in links]
##print (actual_web_links)
##
##for link in links:
##	print ("\n\nLinks:",link.text)



##urls=[]
##for link in soup.findAll('a'):
##	print(link.get('href'))

# pcs=[]

# for i in htmllist:
#     soup = BeautifulSoup(i.text, 'html.parser')
#     linklist=[]
#     for a in soup.findAll('a'):
#             #a =td.find('a')
#             if 'href' in a.attrs and a.text in ['Download','Open']:
#                     linklist.append(a.get('href'))
#     pcs.append(linklist)


# for i in pcs:
#     print(i,'\n')