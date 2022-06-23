"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from kywapi.models import Wage


class WageView(ViewSet):
    """Wage"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            wage = Wage.objects.get(pk=pk)
            serializer = WageSerializer(wage, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        wages = Wage.objects.all()

        # Note the addtional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = WageSerializer(
            wages, many=True, context={'request': request})
        return Response(serializer.data)
    
class WageSerializer(serializers.ModelSerializer):
    """JSON serializer for wages

    Arguments:
        serializers
    """
    class Meta:
        model = Wage
        fields = ('id', "title", "company","salary","city",
        "work_state","year","source")