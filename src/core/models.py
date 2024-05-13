import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class SoftDeletionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False,
                                  verbose_name=_('deleted'))

    objects = SoftDeletionManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    class Meta:
        abstract = True


class AuditTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('updated_at'))

    class Meta:
        abstract = True


class AuditUserModel(models.Model):
    created_by = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='created_by',
        related_query_name='created_by',
        verbose_name=_('created_by')
    )
    updated_by = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='updated_by',
        related_query_name='updated_by',
        verbose_name=_('updated_by')
    )

    class Meta:
        abstract = True


class AuditModelMixin(AuditTimeStampModel, AuditUserModel):

    class Meta:
        abstract = True
