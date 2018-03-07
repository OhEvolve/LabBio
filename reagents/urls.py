
# nonstandard libraries 
from django.urls import path

# homegrown libraries
from . import views

app_name = 'reagents'
urlpatterns = [
               path('liquid/<int:pk>/', views.LiquidView.as_view(), name='liquid'),
               path('solid/<int:pk>/', views.SolidView.as_view(), name='solid'),
               path('biologic/<int:pk>/', views.BiologicView.as_view(), name='biologic'),
               path('solution/<int:pk>/', views.SolutionView.as_view(), name='solution'),
              ]
