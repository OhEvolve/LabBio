
# nonstandard libraries 
from django.urls import path

# homegrown libraries
from . import views

app_name = 'reagents'
urlpatterns = [
               path('<int:pk>/', views.ReagentView.as_view(), name='reagent'),
              ]
