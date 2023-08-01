from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            username = nickname,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    # 관리자 user 생성
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self.db)
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(max_length=100, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # username field를 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'nikcname']

    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True