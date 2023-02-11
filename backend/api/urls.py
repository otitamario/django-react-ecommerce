from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet


app_name = "api"

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = router.urls
