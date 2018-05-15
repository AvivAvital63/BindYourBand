import socket  # Import socket module
import thread

def serverSettings():
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 7777  # Reserve a port for your service.

    print 'Server started!'
    print 'Waiting for clients...'

    s.bind((host, port))  # Bind to the port
    s.listen(5)  # Now wait for client connection.

    while True:
        c, addr = s.accept()  # Establish connection with client.
        print 'Got connection from', addr
        thread.start_new_thread(on_new_client, (c, addr))

    s.close()

def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        # do some checks and if msg == someWeirdSignal: break:
        print addr, ' >> ', msg
        msg = raw_input('SERVER >> ')
        clientsocket.send(msg)
    clientsocket.close()


if __name__ == "__main__":
    serverSettings()
