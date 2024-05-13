from django.db import models


# class User(models.Model):
#     user_id = models.UUIDField(primary_key=True)
#     user_name = models.CharField(max_length=255)
#     user_bio = models.TextField()
#     is_author = models.BooleanField(default=False)
#
#     def __str__(self):
#         return (
#             'User:\n'
#             f'\tname: {self.user_name}'
#             f'\tuuid: {self.user_id}',
#         )
