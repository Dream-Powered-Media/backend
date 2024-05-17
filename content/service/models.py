import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=500, blank=True)
    is_author = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return 'Profile:\n' \
            f'\tname: {self.user.name}' \
            f'\tbio: {self.user_bio}'

    
class Media(models.Model):
    media_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    media_name = models.CharField(max_length=255)
    media_type = models.CharField(max_length=255)
    media_link = models.CharField(max_length=255)
    author_link = models.CharField(max_length=255, null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)

    def __str__(self):
        return 'Media:\n' \
            f'\tname: {self.media_name}' \
            f'\tuuid: {self.media_id}'


class MediaLink(models.Model):
    media_link_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    directory_parent = models.ForeignKey('Directory', on_delete=models.PROTECT, null=True, default=None)
    related_community = models.ForeignKey('Community', on_delete=models.CASCADE)
    grade_val = models.FloatField(default=0)
    admin_grade_val = models.FloatField(default=0)
    grade_count = models.IntegerField(default=0)
    admin_grade_count = models.IntegerField(default=0)

    def __str__(self):
        return 'MediaLink:\n' \
            f'\tname: {self.media.name}' \
            f'\tuuid: {self.media_link_id}'



class Directory(models.Model):
    directory_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    directory_parent = models.ForeignKey('Directory', on_delete=models.PROTECT, null=True)
    related_community = models.ForeignKey('Community', on_delete=models.CASCADE, null=True)
    directory_name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)

    def __str__(self):
        return 'Directory:\n' \
            f'\tname: {self.directory_name}' \
            f'\tuuid: {self.directory_id}'


class Community(models.Model):
    community_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    community_name = models.CharField(max_length=255)
    community_description = models.TextField()

    def __str__(self):
        return 'Community:\n' \
            f'\tname: {self.community_name}' \
            f'\tuuid: {self.community_id}'


class AuthorRequest(models.Model):
    author_request_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    mail = models.CharField(max_length=255)
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return 'AuthorRequest:\n' \
            f'\trequest: {self.user.name}'


class RoleRequest(models.Model):
    role_request_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)
    community_id = models.UUIDField()
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return 'RoleRequest:\n' \
            f'\tuser_id: {self.user.primary_key}' \
            f'\trole_id: {self.role.primary_key}'


class Action(models.Model):
    action_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    action_name = models.CharField(max_length=255)
    role_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return 'Action:\n' \
            f'\tname: {self.action_name}' \
            f'\tuuid: {self.action_id}'


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True, auto_created=True, default=1)
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return 'Role:\n' \
            f'\tname: {self.role_name}' \
            f'\tuuid: {self.role_id}'


class UserAction(models.Model):
    user_action_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True)
    community = models.ForeignKey('Community', on_delete=models.CASCADE, null=True)
    details = models.CharField(max_length=255)

    def __str__(self):
        return 'UserAction:\n' \
            f'\tuser_id: {self.user.primary_key}' \
            f'\tself_id: {self.user_action_id}' \
            f'\taction_id: {self.action.primary_key}' \
            f'\tcomm_id: {self.community.primary_key}'


class Grade(models.Model):
    grade_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    grade_value = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)
    media_link = models.ForeignKey('MediaLink', on_delete=models.CASCADE)

    def __str__(self):
        return 'Grade:\n' \
            f'\tuser: {self.user.name}' \
            f'\tself_id: {self.grade_id}' \
            f'\tmedia: {self.media_link.name}' \
            f'\tvalue: {self.grade_value}'


class Relation(models.Model):
    rel_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    community_id = models.ForeignKey('Community', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return 'Relation:\n' \
            f'\tuser: {self.user.primary_key}'
