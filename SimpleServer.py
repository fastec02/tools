#!/usr/bin/python3

import http.server
import socketserver
import sys

args = sys.argv

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

if(len(args) > 2):
	print("Error: ./SimpleServer.py <PORT>")
	sys.exit()
elif(len(args) == 2):
	PORT = int(args[1])

with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print("serving at port", PORT)
	httpd.serve_forever()
