#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search4.py

# (The Google API originally used in this example now requires API keys,
#  so here's an alternative that calls openstreetmap.org.)

import socket
import ssl
from urllib.parse import quote_plus

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Example 4\r\n\ 
Connection: close\r\n\
\r\n\ 
"""

def geocode(address):
    unencrypted_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443)) # ip(hoac ten mien) +port
    sock = ssl.wrap_socket(unencrypted_sock) #bao mat
    request = request_text.format(quote_plus(address))

    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more #raw_reply = raw_reply + more
    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('Bac Tu Liem District, Hanoi')
