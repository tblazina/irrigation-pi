#!/bin/bash
echo "Pulling latest main branch from GitHub..."
git checkout main
git pull

echo "installing python packages with uv..."
uv sync

echo "Restarting Uvicorn server..."
uv run irrigation-pi restart uvicorn

echo "Restarting nginx server..."
uv run irrigation-pi restart nginx

echo "Irrigation Pi application was updated and is now available on http://raspberrypi.local"
