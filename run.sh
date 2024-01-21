#!/bin/bash

gunicorn api:app \
    --chdir ./src/fast_guni_app
    --workers=1 \
    --bind=0.0.0.0 \
    --worker-class=uvicorn.workers.UvicornWorker \
    --logger-class=fast_guni_app.logging.UnifiedLogger