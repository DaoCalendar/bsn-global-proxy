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
import requests
def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def parse_args(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Proxy BSN requests')
    parser.add_argument('--port', dest='port', type=int, default=8114,
                        help='serve HTTP requests on specified port (default: 8114)')
    parser.add_argument('--bsn-url', dest='bsn_url', required=True,
                        help='bsn url')
    parser.add_argument('--api-key', dest='api_key', required=True,
                        help='bsn api key')
    parser.add_argument('--x-api-sub-path', dest='api_sub_path', required=False,default="web3_clientVersion",
                        help='bsn api sub path')
    args = parser.parse_args(argv)
    return args

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    print('http server is starting at http://localhost:{}/rpc and http://localhost:{}/indexer for node and indexer service...'.format(args.port, args.port))
    server_address = ('127.0.0.1', args.port)
    bsn_url = args.bsn_url
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': args.api_key,
    }
    xapisubpath = args.api_sub_path
    payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\"" + ":\"" + xapisubpath + "\",\n\t\"params\":[],\n\t\"id\":1\n}"
    print(payload)
    response = requests.request(method="POST", url=bsn_url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


