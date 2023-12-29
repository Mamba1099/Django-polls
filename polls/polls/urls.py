
from .views import QuestionViewSet
from rest_framework.routers import DefaultRouter

"""_
Generate URL pattern for API views based on action defined

"""
router = DefaultRouter()
router.register('', QuestionViewSet, basename='questions')
urlpatterns = router.urls #assing generated URL patterns to urlpatterns