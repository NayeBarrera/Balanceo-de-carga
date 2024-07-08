FROM python:3.10
#crear un directorio de trabajo
WORKDIR /Servidor2
COPY servidor2.py .
#instala las dependencias necesarias
RUN pip install flask

#ejecutar la aplicacio
CMD [ "python","servidor2.py" ]

EXPOSE 5000