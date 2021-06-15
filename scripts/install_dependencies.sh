#! /bin/bash

if [[ "$ENV" == "development" ]]; then
  pip install --no-cache-dir -r requirements.txt --user
else
  pip install --no-cache-dir -r requirements-prod.txt --user
fi

