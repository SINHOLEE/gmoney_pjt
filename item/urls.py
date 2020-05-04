from django.urls import path
from . import views 


app_name = 'item'  # 이름 지정하기
urlpatterns = [
    path('get_json/', views.get_json, name='get_json' ),
]

