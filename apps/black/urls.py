from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokes$', views.pokes),
    url(r'^button$', views.button),

]
