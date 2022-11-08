FROM python:3.10.5-slim
RUN cat /etc/os-release
RUN apt-get update && apt-get install -y \
    curl apt-utils \
    curl \
    wget \
    gnupg \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - &&\
    curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list &&\
    wget https://packages.microsoft.com/debian/11/prod/pool/main/m/msodbcsql17/msodbcsql17_17.10.1.1-1_amd64.deb 
RUN ACCEPT_EULA=Y apt-get install -y ./msodbcsql17_17.10.1.1-1_amd64.deb
ADD requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -q -r requirements.txt
COPY . /app
WORKDIR /app
CMD python manage.py runserver 0.0.0.0:$PORT
