from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

class Snack:
    def __init__(self, name, rank=100):
        self.name = name
        self.rank = rank

    def serialize(self):
        return vars(self)

snacks = []
snacks.append(Snack('snickers',1))    
snacks.append(Snack('cheesy poofs'))


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_path = urlparse(self.path)

        print('request path', parsed_path.path)

        parsed_qs = parse_qs(parsed_path.query)

        print('parsed query', parsed_qs)
        
        
        if parsed_path.path == '/snacks':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            safe_snacks = [ snack.serialize() for snack in snacks ]

            json_string = json.dumps(safe_snacks)
            self.wfile.write(json_string.encode())
            return

        if parsed_path.path == '/locations':
            query = 'barcelona'
            api_key = 'AIzaSyCz4_13_FImCJdgbqeWYrglhmkcBRW5mgg'
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}';
            print('url', url)


            result = requests.get(url).json()

            # this.formatted_query = res.body.results[0].formatted_address;
            
            formatted_query = result['results'][0]['formatted_address']

            print('fq', formatted_query)

            self.wfile.write(b'tbd')
            return

        self.send_response_only(404)
        self.end_headers()

    def do_POST(self):
        pass

    def do_PUT(self):
        pass

    def do_HEAD(self):
        pass

    




def create_server():
    return HTTPServer(
        ('127.0.0.1', 3000), SimpleHTTPRequestHandler
    )

def run_forever():
    server = create_server()

    try: 
        print(f'Starting server on port 3000')
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()
