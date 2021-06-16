#! /bin/bash

if [[ "$ENV" == "development" ]]; then
  pip install --no-cache-dir -r requirements-dev.txt --user
else
  pip install --no-cache-dir -r requirements-prod.txt --user
fi

