import django_filters
from django_filters import CharFilter,DateFilter

from .models import *

class ReportdetailsFilter(django_filters.FilterSet):
    workdesc=CharFilter(field_name='workdesc',lookup_expr='icontains',label='شرح کار')
    Date=CharFilter(field_name='Date',lookup_expr='icontains',label='تاریخ')
    fullname=CharFilter(field_name='fullname',lookup_expr='icontains',label='نام')
    tag=CharFilter(field_name='tag',lookup_expr='icontains',label='تگ')
    otherworkdesc=CharFilter(field_name='otherworkdesc',lookup_expr='icontains',label='ادامه کار')
    
    #Date=DateFilter(field_name='Date',lookup_expr='e')
    class Meta:
        model=reportdetails
        fields=['workdesc','fullname','tag','otherworkdesc','Date']
        