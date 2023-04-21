FROM postgres:latest
ENV POSTGRES_PASSWORD=pass
COPY estate.sql /docker-entrypoint-initdb.d/
