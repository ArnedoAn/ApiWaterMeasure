# Usamos una imagen base de Python
FROM python:3.9

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requisitos y lo instalamos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiamos todo el contenido del directorio actual al directorio /app en el contenedor
COPY . .

# Exponemos el puerto 5000 (o el puerto que estés usando en tu aplicación Flask)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "src/app.py"]
