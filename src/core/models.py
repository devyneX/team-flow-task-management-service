import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False,
                                  verbose_name=_('deleted'))

    objects = BaseModelManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    class Meta:
        abstract = True


class AuditTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        abstract = True


class AuditUserModel(models.Model):
    created_by = models.UUIDField()
    updated_by = models.UUIDField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_by = self.created_by
        super().save(*args, **kwargs)


class AuditModelMixin(AuditTimeStampModel, AuditUserModel):

    class Meta:
        abstract = True
