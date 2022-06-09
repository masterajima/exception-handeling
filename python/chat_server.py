"""for server multithreaded chat application"""
from socket import AF_INET, SO_REUSEADDR,socket,SOCK_STREAM
from threading import Thread

##server ip address
SERVER_HOST='0.0.0.0'
SERVER_PORT=5002
seprator_token='<>'#seorate client name and message

#initialize all connected client socket
client_soket=set()
#create TCP socket
s=socket.socket()
#make port reusable
s.setsockopt(socket.SOL_SOCKET,SO_REUSEADDR,1)
#bind the socket
s.bind((SERVER_HOST,SERVER_PORT))
#listen for coming connection
s.listen(5)
print()

## code for server
def listen_for_client(cs):
    """
    This function keep listen for message from client socket
    """
    while True:
        try:
        #keep listening connection from cient socket
           msg=cs.recv(1024).decode()
        #if no longer client connected remove from set
        except Exception as e:
          client_soket.remove(cs)
          catch:msg=msg.replace(seprator_token,':')
    for client_soket in client_soket:
        #send message to client
        client_soket.send(msg.encode())

while True:
    #keep listen for new connection
    client_soket,client_address=s.accept()
    print(f"[+]client address connected")
    #add new client to connected socket
    