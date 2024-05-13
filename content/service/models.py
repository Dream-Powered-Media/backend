from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_bio = models.TextField()
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return (
            'User:\n'
            f'\tname: {self.user_name}'
            f'\tuuid: {self.user_id}',
        )

    
class Media(models.Model):
    media_id = models.UUIDField(primary_key=True)
    media_name = models.CharField(max_length=255)
    media_type = models.CharField(max_length=255)
    media_link = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    author_link = models.CharField(max_length=255)
    author_id = models.ForeignKey('User', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return (
            'Media:\n'
            f'\tname: {self.media_name}'
            f'\tuuid: {self.media_id}',
        )


class MediaLink(models.Model):
    media_link_id = models.UUIDField(primary_key=True)
    media_link_name = models.CharField(max_length=255)
    media_id = models.ForeignKey('Media', on_delete=models.PROTECT, null=True)
    directory_parent = models.UUIDField()
    related_community = models.UUIDField()
    grade = models.IntegerField()

    def __str__(self):
        return (
            'MediaLink:\n'
            f'\tname: {self.media_link_name}'
            f'\tuuid: {self.media_link_id}',
        )


class Directory(models.Model):
    directory_id = models.UUIDField(primary_key=True)
    directory_parent = models.ForeignKey('Directory', on_delete=models.PROTECT, null=True)
    related_community = models.ForeignKey('Community', on_delete=models.PROTECT, null=True)
    directory_name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    level = models.IntegerField(null=True)

    def __str__(self):
        return (
            'Directory:\n'
            f'\tname: {self.directory_name}'
            f'\tuuid: {self.directory_id}',
        )


class Community(models.Model):
    community_id = models.UUIDField(primary_key=True)
    community_name = models.CharField(max_length=255)
    community_description = models.TextField()

    def __str__(self):
        return (
            'Community:\n'
            f'\tname: {self.community_name}'
            f'\tuuid: {self.community_id}',
        )


class AuthorRequest(models.Model):
    author_request_id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    mail = models.CharField(max_length=255)
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return (
            'AuthorRequest:\n'
            f'\tuser_id: {self.user_id}',
        )


class RoleRequest(models.Model):
    role_request_id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    role_id = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
    community_id = models.UUIDField()
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return (
            'RoleRequest:\n'
            f'\tuser_id: {self.user_id}'
            f'\trole_id: {self.role_id}',
        )


class Action(models.Model):
    action_id = models.UUIDField(primary_key=True)
    action_name = models.CharField(max_length=255)
    role_id = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return (
            'Action:\n'
            f'\tname: {self.action_name}'
            f'\tuuid: {self.action_id}',
        )


class Role(models.Model):
    role_id = models.UUIDField(primary_key=True)
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return (
            'Role:\n'
            f'\tname: {self.role_name}'
            f'\tuuid: {self.role_id}',
        )
