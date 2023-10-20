from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from config.permissions import *
from user_manager.models import Node


class NodeViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Node.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # import ipdb;
        # ipdb.set_trace()
        fields = request.GET.get('fields')
        print(fields)
        node = Node.objects.get(id=kwargs["pk"])
        print(node)
        return Response(status=status.HTTP_200_OK)
