# Daphne handles both HTTP and WebSocket connections.
# gunicorn does NOT support WebSockets, so we use Daphne.
web: daphne -b 0.0.0.0 -p $PORT job_portal.asgi:application

# 'release' runs automatically on every Railway/Render deploy
# before the web process starts. Safe to run multiple times.
release: python manage.py migrate --no-input && python manage.py collectstatic --no-input --clear
