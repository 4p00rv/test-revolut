#!/bin/bash

if [[ "$ENV" == "development" ]]; then
  python -m flask run -p $PORT --host=0.0.0.0
else
  gunicorn -b 0.0.0.0:$PORT 'server:app'
fi

