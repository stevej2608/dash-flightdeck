from holoniq.utils import set_level
import dash_labs as dl

from app import create_app
from server import serve_app

app = create_app(dl.plugins.page_container)

if __name__ == "__main__":
    set_level("INFO")
    serve_app(app, debug=False)
