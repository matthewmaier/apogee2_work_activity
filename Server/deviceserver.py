#!/usr/bin/env python

import sys, getopt, os
import time
import socket
import SocketServer

input_file = None
server = None

def main(argv):
    """
    Sets up and starts our TCP data server
    """
    global server

    # Get our command line options and arguments, and warn the user of incorrect usage
    try:
        opts, args = getopt.getopt(argv, "hf:")
    except getopt.GetoptError:
        print 'deviceserver.py -f <inputfile>'
        sys.exit(2)

    # Handle the command line options and their arguments
    for opt, arg in opts:
        if opt == '-h':
            print 'deviceserver.py -f <inputfile>'
            print 'Example: deviceserver.py -f 2013_6_11_15_8_37.csv'
            print '-f: Specifies the Shepard data file to serve to the client(s)'
            sys.exit()
        elif opt == '-f':
            global input_file
            input_file = arg

    # Where our client UI will connect
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on the given port
    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)

    # Doesn't seem to necessarily help with a SocketServer object
    # Make sure we don't get locked out of the port when hitting CTRL-C
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Waiting on client to connect and request streaming...")

    # Activate the server; this will keep running until you interrupt the program with Ctrl-C
    server.serve_forever()

    sys.exit(0)


class TCPHandler(SocketServer.BaseRequestHandler):
    """
    Handles TCP requests from our client UI
    """

    in_data = None  # The data coming from the client
    f = None  # The file that we're streaming to the client

    def handle(self):
       # Don't dump our client after the first send
        while True:
            # The client has to ask to start the data streaming
            self.in_data = self.request.recv(1024).strip()

            # Check to see if the client is ready for data streaming
            if self.in_data.decode("utf-8") == "R":
                # Open the data file for reading
                self.f = open(input_file, 'r')

                last_time = -1.0

                # Begin streaming the data to the client
                for line in self.f:
                    # Skip the first header line
                    if line.split(',')[0][0] == 'T':
                        continue

                    # The line contains the timestamp
                    cur_time = float(line.split(',')[0])

                    # Pull the amount of delay into the send dictated by the timestamps
                    if last_time == -1.0:
                        delay = 0.0
                    else:
                        # The delay between our samples (could vary depending on orig data speeds)
                        delay = cur_time - last_time

                    # Add the appropriate amount of delay
                    time.sleep(delay)

                    # Set up for the next round
                    last_time = cur_time

                    self.request.sendall(bytes(line))
            elif self.in_data.decode("utf-8") == "Q":
                global server

                print("Shutting down server.")

                # Clean up after ourselves and exit
                if self.f is not None:
                    self.f.close()

                # TODO: This should work, but usually hangs waiting for the server to shutdown
                # Attempt to gracefully shut the server down
                #server.shutdown()

                # Do a hard exit since this will be running in another thread
                os._exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
