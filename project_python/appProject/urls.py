from django.urls import path
from .views import index, upload_excel

urlpatterns = [
    path("", index, name="home"),
    path("upload_excel", upload_excel, name="upload_excel"),

]