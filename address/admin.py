from django.contrib import admin
from address.models import Address
# Register your models here.
# Admin 에 등록하는 모델을 작성
class AddressAdmin(admin.ModelAdmin): # 상속받았다
    list_display = ('name', 'tel', 'email', 'address')
    # idx 는 sequence 처럼 자동 생성이므로 생략 가능
    # 관리자 화면에 출력될 필드 목록을 튜플로 정의한다. ***

# 관리자 화면에서 우리가 만든 Address와 AddressAdmin 모델을 직접 관리하도록 등록한다.
admin.site.register(Address,AddressAdmin)
