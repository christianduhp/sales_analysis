from app import app as dash_app, init_app

init_app()

if __name__ == "__main__":
    dash_app.run_server(debug=True)
