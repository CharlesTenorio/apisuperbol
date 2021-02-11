from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
  openapi.Info(
    title="App Api",
    default_version='v1',
    description="",
    terms_of_service="https://joaofilho.dev/",
    contact=openapi.Contact(email="devdrummerzzz@gmail.com"),
    license=openapi.License(name="Copyright License"),
  ),
  public=True,
  permission_classes=[]
)
