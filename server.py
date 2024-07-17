from os import getcwd,chdir
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the HTTP request handler class
class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    # Override the default behavior for the GET request
    def do_GET(self):
        # Set the response status code
        self.send_response(200)
        
        # Set the Content-Type header
        self.send_header('Content-type', 'text/html')
        
        # End headers (this must be called after each header set)
        self.end_headers()
        
        # Open and read the HTML file
        with open('index.html', 'rb') as file:
            # Send the HTML content to the client
            self.wfile.write(file.read())

# Define the server address (server IP and port)
server_address = ('', 5555)  # Leave the host empty to accept connections on all available IPv4 interfaces

# Create an HTTP server with our custom handler
httpd = HTTPServer(server_address, MyHttpRequestHandler)

# Output a simple message to indicate the server is running
print('Server running on port 5555...')

# Start the HTTP server
httpd.serve_forever()
