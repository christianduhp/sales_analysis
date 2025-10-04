from app import app as dash_app
import app.layouts  # garante que o layout é carregado
import app.callbacks  # garante que os callbacks são carregados

if __name__ == "__main__":
    dash_app.run_server(debug=True)
