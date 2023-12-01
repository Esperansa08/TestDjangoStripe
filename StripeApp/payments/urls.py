from django.urls import path
from payments import views


urlpatterns = [
    path('buy/<id>', views.buy_item, name='buy_item'),
    path('item/<id>', views.get_item),
]
