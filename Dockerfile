FROM python:3.10.0b2-buster

# Install dumb-init
RUN apt-get update && apt-get install -y dumb-init
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
ENV PORT 8080
EXPOSE 8080

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["./scripts/start.sh"]
