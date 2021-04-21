from rest_framework import routers
from .views import SurveyViewset, ChoiceViewset

router = routers.DefaultRouter()
router.register('survey', SurveyViewset, basename='survey')
router.register('choice',ChoiceViewset, basename='choice')
urlpatterns = router.urls
