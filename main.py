from usage import app

# uwsgi stub, referenced in uwsgi.ini

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
