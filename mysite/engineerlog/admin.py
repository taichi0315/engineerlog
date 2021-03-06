from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import AppUser, Post

class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = '__all__'

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email','displayname')

class AppUserAdmin(UserAdmin):
    fieldsets = (
        (None,      {'fields': ('username','password')}),
        (_('email'),      {'fields': ('email',)}),
        (_('displayname'),      {'fields':('displayname',)}),
        (_('Permissions'),{'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('icon'),      {'fields': ('icon',)}),
        (_('profile_sentence'),      {'fields': ('profile_sentence',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    form = AppUserChangeForm
    add_form = AppUserCreationForm
    list_display = ('username', 'email', 'displayname', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username',)
    ordering = ('username',)

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('作成者',      {'fields': ('created_user',)}),
        ('勉強時間',        {'fields': ('duration',)}),
        ('コメント',         {'fields': ('comment',)}),
    )
    search_fields = ('username',)

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Post, PostAdmin)