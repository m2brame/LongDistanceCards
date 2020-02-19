import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

class myHandler(BaseHTTPRequestHandler):
    allowedGetURLS = ["join","help"]

    #Handler for the GET requests
    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(b"Hello World!")
        return

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    try:
        # Create the server, binding to localhost on port 9999
        with HTTPServer((HOST, PORT), myHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting Down\n")
        server.socket.close()