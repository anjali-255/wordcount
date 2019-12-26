from django.urls import path
from . import veiws

urlpatterns = [
    path('', veiws.home),
    path('count/', veiws.count, name='count'),
    path('about/', veiws.about, name='about'),
   ]
