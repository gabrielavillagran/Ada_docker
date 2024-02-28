# definindo que é python e qual versao 
FROM python:3

# da update nos pacotes do ubuntu e trazendo o instalar de pacotes do python
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev

# define um diretório de trabalho para outras instruções Dockerfile, como RUN , CMD e também o diretório de trabalho para executar instâncias da imagem do contêiner
WORKDIR /app

RUN pip install Flask requests flask_mysqldb bootstrap-flask

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]