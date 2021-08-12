import socket

HOST = '127.0.0.1'
PORT = 55555
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))



def scan(target,port):
    try:
        sn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sn.connect((target, int(port)))
        return True
    except:
        return False

def range_scan(target,ports):
    ports = ports.split('-')
    open_ports = []
    for p in range(ports[0],ports[1]):
        if scan(target,p) == True:
            open_ports.append(p)
    if open_ports == []:
        return None
    else:
        open_ports = str(open_ports)
        open_ports = open_ports.replace(',','-').replace('[','').replace(']','')
        return open_ports





def main():
    while True:
        message = sock.recv(1024)
        message = message.decode('utf-8')
        message = message.split(',')
        if message[-1] == 'b':
            oport = range_scan(message[0], message[1])
            if oport != None:
                sm = f"{oport}, {message[2]} , s"
                sock.send(sm.encode('utf-8'))



# 142.250.180.46

if __name__ == "__main__":
    try:
        main()
    except :
        sock.close()