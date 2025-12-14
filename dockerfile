FROM python:3.12-alpine

# Evita cache e arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências de sistema (necessárias para psycopg2 e pandas)
RUN apk update && apk add --no-cache \
    build-base \
    libpq \
    libpq-dev \
    python3-dev \
    musl-dev \
    gcc \
    postgresql-dev

# Copia requirements primeiro (cache)
COPY requirements.txt .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia o código da aplicação
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
