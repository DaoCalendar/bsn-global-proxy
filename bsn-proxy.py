#!/usr/bin/env python

#  from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import socket
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import argparse
import os
import random
import sys
from urllib import request as urllib2

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def set_header():
    headers = {
        #  'Host': hostname
        'X-API-KEY': args.api_key
    }

    return headers

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'
    def do_HEAD(self):
        self.do_GET(body=False)

    def do_GET(self, body=True):
        req_header = self.parse_headers()

        del req_header['Host']
        resp = urllib2.Request(url=bsn_url,
                               headers=merge_two_dicts(dict(req_header), set_header()),
                               )

        r = urllib2.urlopen(resp)

        self.send_response(r.getcode())
        for k, v in r.getheaders():
            self.send_header(k, v)
        self.end_headers()

        if body:
            self.wfile.write(r.read())
        return

    def do_POST(self, body=True):
        # print(self.headers)
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        req_header = self.parse_headers()
        del req_header['Host']

        # print(bsn_url)
        resp = urllib2.Request(url=bsn_url,
                               headers=merge_two_dicts(dict(req_header), set_header()),
                               data=post_body)

        r = urllib2.urlopen(resp)
        sent = True

        self.send_response(r.getcode())
        for k, v in r.getheaders():
            self.send_header(k, v)
        self.end_headers()

        if body:
            self.wfile.write(r.read())
        return

    def parse_headers(self):
        return self.headers

    def send_resp_headers(self, resp):
        respheaders = resp.headers
        for key in respheaders:
            if key not in ['Content-Encoding', 'Transfer-Encoding', 'content-encoding', 'transfer-encoding', 'content-length', 'Content-Length']:
#                print key, respheaders[key]
                self.send_header(key, respheaders[key])
        self.send_header('Content-Length', len(resp.content))
        self.end_headers()



def parse_args(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Proxy BSN requests')
    parser.add_argument('--port', dest='port', type=int, default=9999,
                        help='serve HTTP requests on specified port (default: 9999)')
    parser.add_argument('--bsn-url', dest='bsn_url', required=True,
                        help='bsn url')
    parser.add_argument('--api-key', dest='api_key', required=True,
                        help='bsn api key')
    args = parser.parse_args(argv)
    return args

class ServerThread(Thread):
    def __init__(self, i):
        Thread.__init__(self)
        self.i = i
        self.daemon = True
        self.start()

    def run(self):
        httpd = HTTPServer(server_address, ProxyHTTPRequestHandler, False)

        httpd.socket = sock
        httpd.server_bind = self.server_close = lambda self: None

        httpd.serve_forever()

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    print('http server is starting on port {}...'.format(args.port))
    server_address = ('127.0.0.1', args.port)
    bsn_url = args.bsn_url

    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    sock.listen(5)

    [ServerThread(i) for i in range(100)]
    print('http server is running as reverse proxy')

    while True:
        time.sleep(10)

