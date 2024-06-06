from django.db import models

from src.accounts.utils import get_user_detail_from_ids
from src.core.models import BaseModelManager


class ProjectQuerySet(models.QuerySet):

    def for_user(self, uuid):
        """
        Returns a queryset of projects for a user

        :param uuid: UUID of the user
        :return: QuerySet[Project]
        """
        return self.filter(member__user=uuid)

    def with_members(self):
        """
        Returns a queryset of projects with prefetched members
        :return: QuerySet[Project]
        """
        return self.prefetch_related('members')

    def with_member_details(self):
        """
        Fetches user information for members of a project
        returns the list of projects and a list of dicts with user information

        :return: QuerySet[Project], Dict[UUID, Dict[str, Any]]
        """
        queryset = self.with_members()
        member_uuids = queryset.values_list('member__user', flat=True)

        member_details = get_user_detail_from_ids(member_uuids)

        return queryset, member_details


class ProjectManager(BaseModelManager):

    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db, query=super().get_queryset().query)

    def for_user(self, uuid):
        return self.get_queryset().for_user(uuid)

    def with_members(self):
        return self.get_queryset().with_members()

    def with_member_details(self):
        return self.get_queryset().with_member_details()
