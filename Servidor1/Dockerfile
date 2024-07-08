FROM python:3.10
#crear un directorio de trabajo
WORKDIR /Servidor1
COPY servidor1.py .
#instala las dependencias necesarias
RUN pip install flask

#ejecutar la aplicacio
CMD [ "python","servidor1.py" ]

EXPOSE 5000