from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Transpose
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    duration = models.DurationField(_('勉強時間'))
    comment = models.TextField(_('コメント'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.comment
        
class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)

        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class AppUser(AbstractBaseUser, PermissionsMixin):

    username=models.CharField(_('username'), max_length=20, unique=True, primary_key=True, db_index=True)
    email = models.EmailField(_('email address'))
    displayname = models.CharField(_('表示名'), max_length=20)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    icon = ProcessedImageField(
            verbose_name=_('アイコン'),
            upload_to='icons/', 
            processors=[Transpose(), ResizeToFill(50, 50)], 
            format='JPEG',
            options={'quality':60},
            default='icons/default.JPG',
            blank=True
    )
    profile_sentence = models.TextField(_('プロフィール文'), blank=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = AppUserManager()
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


