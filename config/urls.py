from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("EcoLoop Backend Running 🚀")


urlpatterns = [
    path('', home),                    # ✅ root check
    path('admin/', admin.site.urls),  # ✅ admin
    path('api/', include('api.urls')) # ✅ all APIs routed here
]