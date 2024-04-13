from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("supp_trad/", views.supp_trad, name="supp_trad"),
    path("refining/", views.refining, name="refining"),
    path("contact/", views.contact, name="contact"),
]