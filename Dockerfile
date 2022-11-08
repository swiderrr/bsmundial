FROM python:3.10.5-slim
RUN cat /etc/os-release
RUN apt-get update && apt-get install -y \
    curl apt-utils \
    curl \
    gnupg \
    odbcinst \
    odbcinst1debian2 \
    libodbc1 \
    unixodbc 
ADD requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -q -r requirements.txt
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
COPY . /app
WORKDIR /app
CMD python manage.py runserver 0.0.0.0:$PORT
