"""
ASGI entry point — handles both HTTP and WebSocket (chat feature).
Used by Daphne in production.
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'job_portal.settings.production'
)

# Import routing after setting env var so Django initialises correctly
from jobs import routing  # noqa: E402

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(routing.websocket_urlpatterns)
    ),
})
