from django.core.exceptions import PermissionDenied
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# Community


class CommunityAPIViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    @action(methods=['GET'], detail=True)
    def full_info(self, request, pk=None):
        media_list = MediaLink.objects.filter(related_community=pk)
        dirs_list = Directory.objects.filter(related_community=pk)
        community = Community.objects.get(pk=pk)
        relations = Relation.objects.filter(community_id=pk)
        return Response({
            'community': CommunitySerializer(community).data,
            'directories': DirectorySerializer(dirs_list, many=True).data,
            'media': MediaLinkSerializer(media_list, many=True).data,
            'relations': RelationSerializer(relations, many=True).data,
        })

    @action(methods=['POST'], detail=True)
    def follow(self, request, pk=None):
        user_id = request.data['user']

        user = User.objects.get(pk=user_id)
        role = Role.objects.get(pk=1)
        community = Community.objects.get(pk=pk)

        new_rel = Relation.objects.create(
            user=user,
            role=role,
            community_id=community,
        )
        return Response({'new_rel': RelationSerializer(new_rel).data})

    @action(methods=['GET'], detail=True)
    def top(self, request, pk=None):
        media_list = MediaLink.objects.filter(related_community=pk).order_by("grade_val")[::-1]
        return Response({'top': MediaLinkSerializer(media_list, many=True).data})

    @action(methods=['POST'], detail=True)
    def request_role(self, request, pk=None):
        # media_list = MediaLink.objects.filter(community_id=pk)
        return Response({'role': None})


# Directory

class DirectoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer

    @action(methods=['POST'], detail=False)
    def add_directory(self, request):
        directory_parent = request.data.get('directory_parent', None)
        community_id = request.data['related_community']

        dir_obj = None
        if directory_parent:
            dir_obj = Directory.objects.get(pk=directory_parent)
        community = Community.objects.get(pk=community_id)

        new_directory = Directory.objects.create(
            directory_parent=dir_obj,
            related_community=community,
        )
        return Response({'new_directory': DirectorySerializer(new_directory).data})


# Media

class MediaAPIViewSet(viewsets.ModelViewSet):
    queryset = MediaLink.objects.all()
    serializer_class = MediaLinkSerializer

    @action(methods=['GET'], detail=False)
    def full_list(self, request):
        _media_list = Media.objects.all()
        return Response({'media_list': MediaSerializer(_media_list, many=True).data})

    @action(methods=['POST'], detail=False)
    def add_media(self, request):
        media_id = request.data['media']
        directory_parent = request.data.get('directory_parent', None)
        community_id = request.data['related_community']

        dir_obj = None
        if directory_parent:
            dir_obj = Directory.objects.get(pk=directory_parent)
        media = Media.objects.get(pk=media_id)
        community = Community.objects.get(pk=community_id)

        new_media_link = MediaLink.objects.create(
            media=media,
            directory_parent=dir_obj,
            related_community=community,
        )
        return Response({'new_media': MediaLinkSerializer(new_media_link).data})



# Role

class RoleAPIViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RelationAPIViewSet(viewsets.ModelViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer


class GradeAPIViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    @action(methods=['POST'], detail=False)
    def grade_media(self, request):
        grade_val = int(request.data['grade_value'])
        user_id = request.data['user']
        role_id = request.data['role']
        media_link = request.data['media_link']


        if role_id < 2:
            raise PermissionDenied('Too weak role')

        currMediaLink = MediaLink.objects.get(pk=media_link)

        if role_id > 2:
            currMediaLink.admin_grade_count += 1
            adm_sum = currMediaLink.admin_grade_val + grade_val
            currMediaLink.admin_grade_val = adm_sum / currMediaLink.admin_grade_count

        currMediaLink.grade_count += 1
        tot_sum = currMediaLink.grade_val + grade_val
        currMediaLink.grade_val = tot_sum / currMediaLink.grade_count

        currMediaLink.save()

        Grade.objects.create(
            grade_value=currMediaLink.grade_val,
            user=User.objects.get(id=user_id),
            role=Role.objects.get(pk=role_id),
            media_link=currMediaLink,
        )
        return Response({'status': 'OK'})


class ProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['GET'], detail=True)
    def full_info(self, request, pk=None):
        profile = Profile.objects.get(user=pk)
        user = User.objects.get(pk=pk)
        rels = Relation.objects.filter(user=pk)

        answer = {
            'id': user.id,
            'name': user.username,
            'bio': profile.user_bio,
            'is_author': profile.is_author,
            'email': user.email,
            'communities': RelationSerializer(rels, many=True).data
        }
        return Response({'full_profile': answer})
