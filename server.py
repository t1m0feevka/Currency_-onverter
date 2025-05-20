from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        login = params.get("login", ["невідомо"])[0]

        content = f"""
        <html>
        <head><meta charset="utf-8"><title>Інформація</title></head>
        <body style="font-family: sans-serif; padding: 2em;">
            <h2>Ваш логін у Moodle: {login}</h2>
            <p><b>Прізвище:</b> Петренко</p>
            <p><b>Ім’я:</b> Софія</p>
            <p><b>Курс:</b> 2</p>
            <p><b>Група:</b> КН-24</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), MyHandler)
    print("Сервер запущено: http://localhost:8080?login=sofiia123")
    server.serve_forever()