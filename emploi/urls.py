from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from iscae_emploi import  views
from django.conf.urls import  handler500,handler404

admin.site.site_title ="ISCAE G-EMPLOI administration"
admin.site.index_title ="ISCAE G-EMPLOI"
admin.site.site_header = "ISCAE"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls',namespace='user') ),

    path('iscae_emploi/', include('iscae_emploi.urls',namespace='iscae_emploi')),




] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)



handler404 = views.handler404
handler500 = views.handler500
