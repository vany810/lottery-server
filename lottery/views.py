from rest_framework.viewsets import mixins, GenericViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema

from lottery.serializers import PrizeSerializer, \
    LotteryActivitySerializer, LotteryRecordSerializer, LotteryRecordCreateSerializer, \
    LotteryUserSerializer, LotteryUserCreateSerializer
from .models import Prize, LotteryRecord, LotteryUser, LotteryActivity


@extend_schema_view(
    list=extend_schema(
        description='抽奖活动列表',
        summary='抽奖活动列表',
        tags=['抽奖接口']
    )
)
class LotteryActivityViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = LotteryActivity.objects.all()
    serializer_class = LotteryActivitySerializer


@extend_schema_view(
    list=extend_schema(
        description='奖品列表',
        summary='奖品列表',
        tags=['抽奖接口']
    )
)
class PrizeViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    filterset_fields = ('activity',)


@extend_schema_view(
    list=extend_schema(
        description='中奖记录列表',
        summary='中奖记录列表',
        tags=['抽奖接口']
    ),
    create=extend_schema(
        description='创建中奖记录',
        summary='创建中奖记录',
        tags=['抽奖接口']
    )
)
class LotteryRecordViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = LotteryRecord.objects.all()
    filterset_fields = ('activity',)

    def get_serializer_class(self):
        if self.action == 'create':
            return LotteryRecordCreateSerializer

        return LotteryRecordSerializer


@extend_schema_view(
    list=extend_schema(
        description='抽奖名单列表',
        summary='抽奖名单列表',
        tags=['抽奖接口']
    ),
    create=extend_schema(
        description='抽奖报名',
        summary='抽奖报名',
        tags=['抽奖接口']
    )
)
class LotteryUserViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = LotteryUser.objects.all()
    filterset_fields = ('activity',)

    def get_serializer_class(self):
        if self.action == 'create':
            return LotteryUserCreateSerializer

        return LotteryUserSerializer
