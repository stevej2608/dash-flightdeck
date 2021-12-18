import logging
from usage import app


if __name__ == "__main__":

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    app.server.run(debug=False, threaded=False)
