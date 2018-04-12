#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import io, sys, _thread, json
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "this is a GET!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        print(self.headers)
        print(self.requestline, self.client_address, self.path)
        b = self.rfile.raw
        #print(b.encode('utf8'))
        #print(self.rfile.read)
        #self.handle()'''

        
        return

# POST
  def do_POST(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Got it, thanks!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
       
        print(self.headers)


        return
 
def runHTTPserver():
  print('starting server...')
   
 
  # Server settings
  server_address = ('', 8080)
  # sys.stderr = open('logfile.txt', 'a')
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  
  httpd.serve_forever()
 
runHTTPserver()

