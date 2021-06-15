FROM python:3.10.0b2-buster
COPY . /app
WORKDIR /app
# Installing pg dependencies for psycopg2
RUN apt-get install -y libpq-dev
RUN pip install -r requirements.txt
