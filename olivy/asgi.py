"""
ASGI config for olivy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import disease_detection.routing  # Import your routing configuration

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olivy.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            disease_detection.routing.websocket_urlpatterns
        )
    ),
})
