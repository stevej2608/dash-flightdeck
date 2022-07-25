import logging

from app import create_app, create_dash


if __name__ == "__main__":

    app = create_app(create_dash)

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    app.run(debug=False, threaded=False)
