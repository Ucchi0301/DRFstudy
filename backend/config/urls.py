from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from api.controllers.group_controller import GroupListView, JoinGroupView
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("groups/", GroupListView.as_view()),
    path("groups/join/", JoinGroupView.as_view()),
]
