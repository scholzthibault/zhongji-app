import http.server, socketserver, datetime, platform, os

PORT = int(os.environ.get("SERVER_PORT", "25565"))

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = (f"<!doctype html><html><head><meta charset=utf-8><title>zhongji</title></head>"
                f"<body style='font-family:sans-serif;background:#16161e;color:#e5e5e5;text-align:center;padding-top:70px'>"
                f"<h1>🟢 zhongji 在线</h1>"
                f"<p>Nodaroo · Sweden SE4 · Python {platform.python_version()}</p>"
                f"<p>服务器时间：{now}</p>"
                f"<p style='color:#888'>port {PORT}</p></body></html>").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a):
        pass

socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), H) as httpd:
    print(f"zhongji status page listening on 0.0.0.0:{PORT}", flush=True)
    httpd.serve_forever()
