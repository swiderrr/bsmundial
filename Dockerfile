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
COPY . /app
WORKDIR /app
CMD python manage.py runserver 0.0.0.0:$PORT
