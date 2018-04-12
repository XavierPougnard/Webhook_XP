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
        with open("logWebhook.txt", "a", encoding='utf8') as fichierLogWH:
          fichierLogWH.write(str(self.headers))
          fichierLogWH.write('\n'+str(self.requestline)+' '+str(self.client_address) +' '+str(self.path)+'\n')
          postbackData=self.rfile.read1(2000)
          fichierLogWH.write(postbackData.decode('utf8'))

        with open("postbackData.txt", "w", encoding='utf8') as fichierpostbackData:
          fichierpostbackData.write(postbackData.decode('utf8'))
        # Ajout d'un attribut dans la structure mentionnant que le message est nouveau. Sera effacé à la lecture
        # l'appel à readlines() insert des '\n' à chaque ligne. Donc suppression ci-dessous. C'est moche...
        with open("postbackData.txt", "r", encoding='utf8') as fichierpostbackData:
          contents = fichierpostbackData.readlines()
        with open("postbackData.txt", "r", encoding='utf8') as fichierpostbackData:
          contentsUnmodified = fichierpostbackData.readlines()
          j=0
          print(len(contents))
          for i in range (0,len(contentsUnmodified)-1):
            if contentsUnmodified[i] == '\n':              
              del contents[i-j]
              j += 1
        contents.insert(1,'    "NEW" : "yes",\n')
        with open("postbackData.txt", "w", encoding='utf8') as fichierpostbackData:
          contents = "".join(contents)
          fichierpostbackData.write(contents)

        print(self.headers)
        print(self.requestline, self.client_address, self.path)
        print(postbackData.decode('utf8'))
        

        return
 
def runHTTPserver():
  print('starting server...')
  #vidage des fichiers de log
  fichierLogWH = open("logWebhook.txt", "w", encoding='utf8')
  fichierLogWH.close()
  with open("postbackData.txt", "w", encoding='utf8') as fichierpostbackData:
    fichierpostbackData.write('{"NEW": "no"}')
  
 
  # Server settings
  server_address = ('192.168.1.17', 36330)
  sys.stderr = open('logfile.txt', 'a')
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  
  httpd.serve_forever()
 
runHTTPserver()

