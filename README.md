# Sakila Project Colab. 4 Peter
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/Mandroide/cms-otek-backend/refs/heads/main/pyproject.toml)

Caso 2 de Sakila para la asignatura de MACDIA.


## Como iniciarse

1. Copiar el archivo `.env.example` y renombrarlo a `.env`
2. Ajustar los valores de cada variable según su ambiente MySQL de Sakila.
3. Activar el ambiente virtual integrado con \envSakilaCrud\Scripts\activate o crear uno nuevo con python -m (nombre del env) venv
4. Ejecutar el comando `pip install -r requirements.txt`
5. Correr la aplicación con el comando `uvicorn app.main:app --reload`
6. Dirigirse a la ruta "http://localhost:8000/docs" para poder interactuar con los recursos mediante la interfaz Swagger UI
