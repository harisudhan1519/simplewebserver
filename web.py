from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html lang="en">
    <body>
        <h1>Configuration Details</h1>

        <h2>Name = S Harisudhan
            <br>
            Reference number = 24004236
             </br>
            
        </h2>
        
        <ul type="none">
            <li><b>Device name</b>          DESKTOP-MOHHBTU</li>
            <li>
               <b>Processor</b> 13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz
            </li>
            <li><b>Installed RAM</b>   16.0 GB (15.7 GB usable)</li>
            <li>
              <b>Device ID</b>  15EEA3B2-7EF5-4DEC-903D-577382C3C005
            </li>
            <li>
                <b>Product ID</b>  00342-42709-00859-AAOEM
            </li>
            <li>
                <b>System type</b> 64-bit operating system, x64-based processor
            </li>
            <li>
                <b>Pen and touch</b> No pen or touch input is available for this display
            </li>
        </ul>


    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()