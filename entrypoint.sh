#!/bin/sh
set -e

# Define a variável FLASK_APP
export FLASK_APP=app.py

# Função para esperar por um serviço
wait_for_service() {
  local host=$1
  local port=$2
  local name=$3

  echo "Waiting for $name..."
  while ! nc -z "$host" "$port"; do
    sleep 1
  done
  echo "$name is up!"
}

# Espera o Postgres
wait_for_service "postgres" 5432 "Postgres"

# Espera o Solr
echo "Waiting for Solr..."
while ! curl -sSf http://solr:8983/solr/cbo >/dev/null 2>&1; do
  sleep 1
done
echo "Solr is up!"

# Inicia o Flask
echo "Starting Flask..."
exec python app.py
