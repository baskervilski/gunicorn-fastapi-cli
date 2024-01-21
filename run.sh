#!/bin/bash

gunicorn fast_guni_app.api:app \
    --workers=1 \
    --bind=0.0.0.0 \
    --worker-class uvicorn.workers.UvicornWorker \
    --logger-class fast_guni_app.logging.UnifiedLogger