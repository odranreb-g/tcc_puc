import os

# bind = "unix:///tmp/nginx.socket"
max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS", "10000"))
max_requests_jitter = int(os.environ.get("GUNICORN_MAX_REQUESTS_JITTER", "100"))
