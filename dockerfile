FROM python:3.12-alpine

# Evita cache e arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema
RUN apk update && apk add --no-cache \
    build-base \
    libpq \
    libpq-dev \
    python3-dev \
    musl-dev \
    gcc \
    postgresql-dev \
    py3-setuptools \
    curl \
    netcat-openbsd

# Copia requirements primeiro (cache eficiente)
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# Copia o código da aplicação
COPY . .

# Copia e dá permissão ao script de entrypoint
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Porta do Flask
EXPOSE 5000

# Define o entrypoint
ENTRYPOINT ["./entrypoint.sh"]
