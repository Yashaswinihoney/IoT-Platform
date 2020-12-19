"""
ASGI config for Platform project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
<<<<<<< HEAD
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import channel.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            channel.routing.websocket_urlpatterns
        )
    ),
})
=======

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform.settings')

application = get_asgi_application()
>>>>>>> 93a9b19... Long Time no C
