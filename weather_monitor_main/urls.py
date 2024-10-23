from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [ # defines the routes of the application
    path('',views.index,name="home"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)