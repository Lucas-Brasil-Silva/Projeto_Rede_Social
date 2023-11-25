from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_rede_social.urls')),
    path('usuario/', include('app_usuarios.urls'))
]

# lucas
# lucasbrasil396@gmail.com
# lucas21013000