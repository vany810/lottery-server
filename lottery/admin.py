from django.contrib import admin
from .models import Prize, LotteryActivity, LotteryUser, LotteryRecord
# Register your models here.


admin.site.register(Prize)
admin.site.register(LotteryActivity)
admin.site.register(LotteryUser)
admin.site.register(LotteryRecord)
