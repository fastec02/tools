#!/usr/bin/python3

import http.server
import socketserver
import argparse
import sys

parser = argparse.ArgumentParser(description="Simple Server by Python.")
parser.add_argument("-p","--port",type=int,default=8000,help="Listen PORT. DEFAULT:8000")

args = parser.parse_args()

Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", args.port), Handler) as httpd:
	print("serving at port", args.port)
	httpd.serve_forever()
