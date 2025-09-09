# Imagem base com Python 3.10
FROM python:3.10-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia os arquivos para o container
COPY . .

# Instala hatchling e as dependências do projeto
RUN pip install --upgrade pip \
 && pip install hatchling \
 && pip install .

# Comando padrão: executa o script CLI "bmi"
CMD ["bmi"]