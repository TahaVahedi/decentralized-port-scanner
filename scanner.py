import subprocess
import platform
import sys
import threading
import socket

HOST = '127.0.0.1'
PORT = 55555
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

# =============== slave section =============


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
        print(open_ports)       # just for test
        return open_ports





def bg():
    while True:
        message = sock.recv(1024)
        message = message.decode('utf-8')
        message = message.split(',')
        if message[-1] == 'b':
            oport = range_scan(message[0], message[1])
            if oport != None:
                sm = f"{oport}, {message[2]} , s"
                sock.send(sm.encode('utf-8'))



# =============== master section =============
def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False


def get_target():
    tgt = str(input("your target: "))
    if ping_ip(tgt):
        return tgt
    else:
        print("target not defined!!")

def ports_proccess(ports):
    ports = ports.split('-')
    ports = range(int(ports[0]), int(ports[1]))
    i = 0
    sendlist = []
    while i < len(ports):
        a = ports[i]
        b = a + 5
        sendlist.append(str(f"{a}-{b}"))
        i += 5
    return sendlist

def get_port():
    ports = str(input("ports_range (for example: 80-100): "))
    return ports_proccess(ports)



def target_sender(target, portlist):
    for i in range(len(portlist)):
        sock.send(f"{target},{portlist[i]},r".encode('utf-8'))

def answer_recieve():
    print("waiting for responds")
    while True:
        rmessage = sock.recv(1024)
        rmessage = rmessage.decode('utf-8')
        rmessage = rmessage.split(',')
        if rmessage[-1] == 'a':
            op = rmessage[0].split('-')
            for l in op:
                print(f"{op[l]} is open.")

def send():
    while True:
        target = get_target()  
        ports = get_port()
        if ping_ip(target):
            try:
                target_sender(target, ports)
                answer_recieve()
            except KeyboardInterrupt:
                sock.close()
                print("app closed")
        else:
            print("target is unavailable")



def main():

    recieve_thread = threading.Thread(target=bg)
    recieve_thread.start()
    send_thread = threading.Thread(target=send)
    send_thread.start()

# 142.250.180.46

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()