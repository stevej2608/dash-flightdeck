import dash_labs as dl

from app import app
from server import serve_app

app.layout = dl.plugins.page_container

if __name__ == "__main__":
    serve_app(app, debug=False)
