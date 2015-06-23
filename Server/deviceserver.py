import glob
import os
import platform
import sys
import time
import socket
import socketserver


def main():
    """Just here to help us test the code incrementally"""    

    # TODO: Grab the file name to stream from the command line arguments
    # TODO: Check to see if a TCP client is connected before starting data transmit
    # Start datastreaming, but spin it off into its own thread with a queue for thread safety
    #t = threading.Thread(target=interface.start_datastreaming)
    #t.daemon = True
    #t.start()

    # Where our client UI will connect
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)

    # TODO: Doesn't seem to help with a SocketServer object
    # Make sure we don't get locked out of the port when hitting CTRL-C
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Waiting on client to connect and request streaming...")

    # Activate the server; this will keep running until you interrupt the program with Ctrl-C
    server.serve_forever()


class TCPHandler(socketserver.BaseRequestHandler):
    """Handles TCP requests from our client UI."""

    in_data = None  # The data coming from the client

    def handle(self):
       # Don't dump our client after the first send
        while True:
            # The client has to ask to start the data streaming
            self.in_data = self.request.recv(1024).strip()

            # Check to see if the client is ready for data streaming
            if self.in_data.decode("utf-8") == "R":
                # TODO: Open the data file for reading
                # Begin streaming the data to the client
                # while True:  # TODO: Send until the end of the file has been reached
                for i in range(0, 10, 1):
                    self.request.sendall(bytes('1.0, 10.0, 100.0\n0.0020,0.44877097,0.0\n0.0040,0.51908207,0.0\n0.0060,0.6597041,0.0\n0.0080,0.7300151,0.0\n0.011,0.8706371,0.0\n0.013,1.327659,0.0\n0.015,1.4331257,0.0\n0.018,1.5737478,0.0\n0.02,1.7143698,0.0\n0.022,2.1713917,0.0\n'))

if __name__ == "__main__":
    main()
