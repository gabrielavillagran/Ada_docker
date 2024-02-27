# pegando a imagem base
FROM mysql:5.7

# copiando o schema.sql para dentro desse diretorio pra iniciar o script sql sozinho
COPY schema.sql /docker-entrypoint-initdb.d/

# deve ser apontada a porta no docker run pois aqui apenas documenta
EXPOSE 3306

# ele nao cria o volume, apenas aponta 
VOLUME ["/backup"]