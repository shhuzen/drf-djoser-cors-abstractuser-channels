
import os
from channels.auth import AuthMiddlewareStack
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from user.consumer import UserConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_asgi_application()



application = ProtocolTypeRouter({
   # Django's ASGI application to handle traditional HTTP requests
   "http": application,


   # WebSocket chat handler
   "websocket": AllowedHostsOriginValidator(
       AuthMiddlewareStack(
           URLRouter([
               path("user/<int:id>/", UserConsumer.as_asgi()),


           ])
       )
   ),
})

