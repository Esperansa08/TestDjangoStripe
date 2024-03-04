from django.urls import path
from .views import success, cancel, index, buy_item, get_item


urlpatterns = [
    path("", index, name="index"),
    path("cancel/", cancel, name="cancel"),
    path("success/", success, name="success"),
    path("item/<id>/", get_item, name="item"),
    path("buy/<id>/", buy_item, name="buy"),
]
