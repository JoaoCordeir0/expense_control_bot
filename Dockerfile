FROM python:3.11-slim

USER root

# Define o fuso horário do container
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Instala pacotes e gera o locale pt_BR.UTF-8
RUN apt-get update && apt-get install -y \
    locales \
    wget \
    gnupg2 \
    curl \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    xdg-utils \
    --no-install-recommends && \
    echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=pt_BR.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

# Define as variáveis de ambiente do locale
ENV LANG=pt_BR.UTF-8 \
    LANGUAGE=pt_BR:pt \
    LC_ALL=pt_BR.UTF-8

# Diretório da aplicação
WORKDIR /app

# Cria e ativa um ambiente virtual
RUN python3.11 -m venv /venv

# Define o ambiente virtual como o padrão
ENV PATH="/venv/bin:$PATH"

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python no ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte para o diretório de trabalho
COPY . .

# Expoẽ a porta 8000
EXPOSE 8000

# Defina o comando padrão para executar o script Python
CMD ["python", "main.py"]