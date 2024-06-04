from src.core.models import BaseModelManager
from src.projects.utils import get_user_detail_from_ids


class ProjectManager(BaseModelManager):

    def get_for_user(self, uuid):
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

        member_details = self.get_member_details(member_uuids)

        return queryset, member_details

    @staticmethod
    def get_member_details(queryset):
        return get_user_detail_from_ids(queryset)
