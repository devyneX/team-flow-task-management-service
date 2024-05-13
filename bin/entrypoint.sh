#!bin/bash

# Collect static files
echo "Collect static files"
python -m src.manage collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python -m src.manage migrate

# Start server
echo "Starting server"
python -m src.manage runserver 0.0.0.0:8000