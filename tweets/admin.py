from django.contrib import admin

from .models import TweetsModel

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = TweetsModel

admin.site.register(TweetsModel, TweetAdmin)