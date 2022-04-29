import http.server
import socketserver
import socket

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

port = 8080
def run():
	global port
	try:
		handler = http.server.SimpleHTTPRequestHandler
		httpd = socketserver.TCPServer(("",port), handler)
		print("Put this address on your friends browser :\n",extract_ip()+":"+str(port))
		print("\nDon't close the app until transfer is complete\n\n")
		print("Got any problem contact the developer\nemail ID: bhavinnor13@gmail.com")
		httpd.serve_forever()
	except:
		port+=1
		run()
run()
