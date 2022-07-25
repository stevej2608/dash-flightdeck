import os
from sys import argv
from waitress import serve
from paste.translogger import TransLogger
from app import create_dash
from usage import create_app
from dash_spa import logging, config

options = config.get('logging')

logging.setLevel(options.level)

logger = logging.getLogger('waitress')
logger.setLevel(logging.WARN)

app = create_app(create_dash)

app_with_logger = TransLogger(app.server, setup_console_handler=False)

# When running in a Docker container the internal port
# is mapped onto a host port. Use the env variables passed
# in to the container to determin the host URL.

port = int(os.environ.get("PORT", 5000))
hostname = os.environ.get("HOSTNAME", "localhost")
hostport = os.environ.get("HOSTPORT", "5000")

print(f'Dash/Flightdeck version 0.0.1')
print(f'Visit http://{hostname}:{hostport}/pages/dashboard')

# serve(app_with_logger, host='0.0.0.0', port=port)

serve(app.server, host='0.0.0.0', port=port)
