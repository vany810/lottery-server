from django.urls import path, include
from rest_framework import routers
from .views import PrizeViewSet, LotteryActivityViewSet, LotteryRecordViewSet, LotteryUserViewSet


router = routers.DefaultRouter()
router.register(r'prize', PrizeViewSet)
router.register(r'activity', LotteryActivityViewSet)
router.register(r'record', LotteryRecordViewSet)
router.register(r'user', LotteryUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
