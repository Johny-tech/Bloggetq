from django_filters import rest_framework as filters
from api.models import Post
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

def get_client_ip(self, request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



class PaginationPosts(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

# D:\not_delete\Back-end\bloggerq   
#this one below is for giving policy for current user briefly it for venv working lifetime ok??!!! Rustam remember this !!! 
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# class MiddleStrarFilter(filters.ModelMultipleChoiceFilter):

#     def get_filter_predicate(self, v):
#         return {'middle_star': v.middle_star}

#     def filter(self,querset,instance):

#         if instance:
#             queryset = queryset.annotate_with_custom_field
#queryset = super().filter(queryset, instance)



class PostFilter(filters.FilterSet):

    category = CharFilterInFilter(field_name = "category__name" , lookup_expr="in")
    author = CharFilterInFilter(field_name='author__user__username', lookup_expr="in")
    date_created = filters.RangeFilter()
    middle_star = filters.CharFilter(field_name='middle_star',lookup_expr="in")

    class Meta:
        model = Post
        fields = ['category', 'date_created','author' , 'middle_star']
