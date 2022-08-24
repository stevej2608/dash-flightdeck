from dash_spa import DashSPA, page_container
from themes import VOLT
from server import serve_app

external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/chartist/0.11.4/chartist.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.2.0/css/all.min.css",
    "https://cdn.jsdelivr.net/npm/notyf@3/notyf.min.css",
    VOLT,
    ]

external_scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js",
    "https://cdn.jsdelivr.net/npm/sweetalert2@11.4.20/dist/sweetalert2.all.min.js",
    "https://cdn.jsdelivr.net/npm/notyf@3/notyf.min.js"
    ]

def create_dash():


    app = DashSPA( __name__,
        prevent_initial_callbacks=True,
        suppress_callback_exceptions=True,
        external_scripts=external_scripts,
        external_stylesheets=external_stylesheets)
    return app


def create_app(dash_factory) -> DashSPA:
    app = dash_factory()
    app.layout = page_container
    app.server.config['SECRET_KEY'] = "A secret key"
    return app

# python app.py

if __name__ == "__main__":
    app = create_app(create_dash)
    serve_app(app, debug=False, path="/pages/dashboard")
