from django.urls import path
from.views import *

urlpatterns = [
    path('', VlogListView.as_view(), name='home'),
    path('post/<int:pk>/', VlogDetailView.as_view(), name='post'),
    path('arab', arab1, name='arab'),
    path('backend', itbackend, name='backend'),
    path('kores', koresuz, name='kores'),
    path('front', itfrontend, name='front'),
    path('tarx', tarix, name='tarx'),
    path('onatli', Onatli, name='onatli'),
    path('kimyo', Kimyo, name='kimyo'),
    path('matem', Matematika, name='matem'),
    path('rus', Rustli, name='rus'),
    path('ingliz', Ingliz, name='ingliz'),
    path('biyo', Biyologiya, name='biyo'),
]
