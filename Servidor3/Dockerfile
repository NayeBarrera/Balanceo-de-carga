FROM python:3.10
#crear un directorio de trabajo
WORKDIR /Servidor3
COPY servidor3.py .
#instala las dependencias necesarias
RUN pip install flask

#ejecutar la aplicacio
CMD [ "python","servidor3.py" ]

EXPOSE 5000