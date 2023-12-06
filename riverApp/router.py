from rest_framework.routers import DefaultRouter
from riverApp.viewSet import StudentViewSet
router = DefaultRouter()

router.register(r'student',StudentViewSet,basename='student')

urlpatterns = router.urls