import socket
import threading, random, sys, uuid

#server connection
HOST , PORT = '127.0.0.1' , 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


# users dict
clients = {} # sid : client



#functions define
def randcast(message,sid): 
    message = str(message[:-1].append(sid).append('b'))
    randomsid = random.choice(clients.keys() != sid)
    client = clients[randomsid]
    client.send(message.encode('utf8'))


def specialcast(message):
    client = clients[message[1]]
    message = str(message[0].append('a'))
    client.send(message.encode('utf8'))


def handle(client,sid):
    while True:
        try:
            message = client.recv(1024)
            message = message.decode('utf-8')
            message = message.split(',')
            switch = message[-1]
            if switch == 'r':       # [<target>,<test_ports>,'r']
                randcast(message,sid)
            elif switch == 's':     # [<open_ports>,<sid>, 's']
                specialcast(message)
            else:
                client.send("your structure not defined!!".encode('utf8'))

            
        except:
            clients.pop(sid)
            client.close()
            break



def recive():
    while True:
        client, addr = server.accept()
        print(addr," is connected")
        s_id = uuid.uuid1()
        clients.update({s_id: client})
        thread = threading.Thread(target=handle, args=(client,s_id,))
        thread.start()





def main():
    # try:
    recive()
    # except:
    #     server.close()
    #     print("server is stopped")
    #     clients.close()
    #     sys.exit()



if __name__ == "__main__":
    print("Starting")
    main()