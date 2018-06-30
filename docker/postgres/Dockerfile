FROM postgres:9.6-alpine

# Override defaults used during initial creation of DB
ENV POSTGRES_USER=nursery \
    POSTGRES_PASSWORD=nursery \
    POSTGRES_DB=nursery \
    PGPASSWORD=nursery \
    PGDATA=/var/lib/postgresql-static/data

RUN mkdir -p /var/lib/postgresql-static/data
