from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from posts.api import router as posts_router

api = NinjaExtraAPI(
    title='Тестовое задание для Asmart',
)

api.register_controllers(NinjaJWTDefaultController)

api.add_router("posts", posts_router, tags=["posts"])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
