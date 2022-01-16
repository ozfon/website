from website import create_app, IO_config

app = create_app()
IO_config()

if __name__ == '__main__':
    app.run(debug=True)