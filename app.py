from flask import Flask
import os
import logging

# Configura il logger di Flask
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("APP_PORT", 5000))
    is_production = str(os.getenv("PRODUCTION", "false")).lower() == "true"
    
    if not is_production:
        logging.info("Running in development mode with Flask's built-in server")
        app.run(host=host, port=port, debug=True)
    else:
        logging.info("Running in production mode with WSGI server")
        from gevent.pywsgi import WSGIServer
        http_server = WSGIServer((host, port), app)
        http_server.serve_forever()
