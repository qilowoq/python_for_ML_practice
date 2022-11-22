from http.server import HTTPServer, BaseHTTPRequestHandler
from isdayoff import IsDayOff
import json
from parameters import *

class HourIncome(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
    
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        data = json.loads(self.rfile.read(content_len))
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        sdo = IsDayOff()
        wd = sdo.number_of_work_days_in_month(2022, 8)
        income = round(data['salary'] / (wd * 8), 2)
        data.update({"hour_income": income})
        self.wfile.write(bytes(str(data), "utf-8"))



if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), HourIncome)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
