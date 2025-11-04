"""
Path -> define o caminho de url e qual função ou view que deve ser executada.
include -> função que vai incluir configurações de outros arquivos de url. Na intenção de dividir
           o roteamento em vários arquivos menores, organizando e deixando mais semântico o código.
django.views.generic -> importa a view genérica do django para exibir um template html.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls', "accounts"), name='accounts'),
    path('game/', include('game.urls', "game"), name='game'),
    path('wallet/', include('wallet.urls', "wallet"), name='wallet'),
]
