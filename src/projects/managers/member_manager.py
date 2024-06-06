from django.db import models

from src.accounts.utils import get_user_detail_from_ids
from src.core.models import BaseModelManager


class MemberQuerySet(models.QuerySet):

    def for_project(self, project):
        """
        Returns a queryset of members for a project
        """
        return self.filter(project=project)

    def with_details(self):
        uuids = self.values_list('user', flat=True)
        return get_user_detail_from_ids(uuids)


class MemberManager(BaseModelManager):

    def get_queryset(self):
        return MemberQuerySet(self.model, using=self._db, query=super().get_queryset().query)

    def for_project(self, project):
        return self.get_queryset().for_project(project)

    def with_details(self):
        return self.get_queryset().with_details()
