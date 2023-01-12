# Rest Framework Imports
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

# Own Imports
from apps.monitor.models import HistoricalStats
from apps.monitor.serializers import HistoricalStatsSerializer


class GetLogsOfHistoricalStatsAPIView(GenericAPIView):

    serializer_class = HistoricalStatsSerializer
    queryset = HistoricalStats.objects.select_related("track")

    def get(self, request: Request):
        historical_stats = self.get_queryset()
        serializer = self.serializer_class(historical_stats, many=True)
        return Response(
            {
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
