FROM python:3.10.0b2-buster

WORKDIR /app

# Set up separate user for server
RUN useradd -r -s /bin/bash worker
RUN chown -R worker:worker /app

USER worker

# set home & current env
ENV HOME /app
ENV PATH="/app/.local/bin:${PATH}"

COPY ./scripts scripts/
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
COPY requirements-prod.txt requirements-prod.txt

ARG ENV
RUN ./scripts/install_dependencies.sh

COPY . .
ENV FLASK_APP=server
EXPOSE 80

CMD ["python", "-m", "flask", "run", "-p", "80", "--host=0.0.0.0"]
