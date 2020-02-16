from django.contrib import admin
from board.models import Board,BBS_comm

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ("pwd","writer","subject","content","regdate")

admin.site.register(Board,BoardAdmin)
#admin.site.register(board_detail)