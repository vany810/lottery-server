from rest_framework import serializers
from .models import Prize, LotteryActivity, LotteryUser, LotteryRecord
from user.serialziers import UserSerializer


class LotteryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryActivity
        fields = '__all__'


class PrizeSerializer(serializers.ModelSerializer):
    activity = LotteryActivitySerializer()

    class Meta:
        model = Prize
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', None)

        super(PrizeSerializer, self).__init__(*args, **kwargs)

        if exclude_fields is not None:
            for field_name in exclude_fields:
                self.fields.pop(field_name)


class LotteryUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryUser
        fields = '__all__'


class LotteryUserSerializer(LotteryUserCreateSerializer):
    activity = LotteryActivitySerializer()
    user = UserSerializer()


class LotteryRecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryRecord
        fields = '__all__'


class LotteryRecordSerializer(LotteryRecordCreateSerializer):
    activity = LotteryActivitySerializer()
    prize = PrizeSerializer(exclude_fields=('activity',))
    user = UserSerializer()

