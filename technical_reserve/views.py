# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sigi_op.views import CustomViewSet
from .serializers import TechnicalReserveSerializer
from .models import TechnicalReserve


class TechnicalReserveListViewSet(CustomViewSet):
    class_name = TechnicalReserve
    order_param_name = 'code'
    queryset = TechnicalReserve.objects.all().order_by('code')
    serializer_class = TechnicalReserveSerializer
