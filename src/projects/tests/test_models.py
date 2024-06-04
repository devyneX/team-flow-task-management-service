import uuid

from django.test import TestCase
from model_bakery import baker

from src.projects.models import Member, Project


class TestProjectModel(TestCase):

    def test_project_creation(self):
        user_uuid = uuid.uuid4()
        project = baker.make(Project, created_by=user_uuid)

        self.assertEqual(project.created_by, user_uuid)
        self.assertEqual(project.owner, user_uuid)

    def test_get_for_user(self):
        user_uuid = uuid.uuid4()
        # user is creator
        projects = baker.make(Project, _quantity=5, created_by=user_uuid)
        baker.make(Project, _quantity=5, created_by=uuid.uuid4())

        for project in projects:
            Member.objects.create(project=project, user=user_uuid, added_by=user_uuid)

        projects = Project.objects.get_for_user(user_uuid)

        self.assertEqual(projects.count(), 5)

        # user is member
        projects = baker.make(Project, _quantity=5, created_by=user_uuid)

        member_uuid = uuid.uuid4()

        for project in projects:
            Member.objects.create(project=project, user=member_uuid, added_by=user_uuid)

        projects = Project.objects.get_for_user(member_uuid)

        self.assertEqual(projects.count(), 5)

    def test_with_members(self):
        uuids = [uuid.uuid4() for _ in range(5)]

        project = baker.make(Project, created_by=uuids[0])

        for user_uuid in uuids:
            Member.objects.create(project=project, user=user_uuid, added_by=uuids[0])

        with self.assertNumQueries(2):
            list(Project.objects.with_members().all())

        project = Project.objects.with_members()

        self.assertEqual(project.count(), 1)
        self.assertEqual(project.first().members.count(), 5)
        self.assertSequenceEqual(project.first().members.values_list('user', flat=True), uuids)

    def test_with_member_details(self):
        project = baker.make(Project, created_by=uuid.uuid4())
        Member.objects.create(project=project, user=project.owner, added_by=project.owner)

        for _ in range(5):
            Member.objects.create(project=project, user=uuid.uuid4(), added_by=project.owner)

        projects, member_details = Project.objects.with_member_details()

        print(projects, member_details)
        self.assertEqual(projects.count(), 1)
        self.assertEqual(projects.first().members.count(), 6)
        # TODO: figure out how to test if the user details are correct

    # def test_get_for_members_x_with_member_details(self):
    # TODO: need to write a custom queryset to have this functionality

    #     project1 = baker.make(Project, created_by=uuid.uuid4())
    #     project2 = baker.make(Project, created_by=project1.owner)
    #
    #     Member.objects.create(project=project1, user=project1.owner, added_by=project1.owner)
    #     Member.objects.create(project=project2, user=project2.owner, added_by=project2.owner)
    #
    #     for _ in range(5):
    #         Member.objects.create(project=project1, user=uuid.uuid4(), added_by=project1.owner)
    #
    #     for _ in range(5):
    #         Member.objects.create(project=project2, user=uuid.uuid4(), added_by=project2.owner)
    #
    #     projects, member_details = Project.objects.get_for_user(project1.owner).with_member_details()
    #
    #     self.assertEqual(projects.count(), 2)
    #     self.assertSequenceEqual(projects, [project1, project2])
    #     self.assertEqual(projects[0].members.count(), 6)
    #     self.assertEqual(projects[1].members.count(), 6)
    #     print(member_details)
