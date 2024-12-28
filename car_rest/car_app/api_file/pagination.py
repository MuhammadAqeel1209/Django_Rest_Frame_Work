from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class ReiviewListPage(PageNumberPagination):
    page_size = 3
    page_query_param ='pa'
    page_size_query_param ='size'
    max_page_size = 1
    last_page_strings ='end'
    
class ReiviewLimitListPage(LimitOffsetPagination):
    default_limit = 1
    max_limit = 2
    offset_query_param ='offset'
    limit_query_param ='limit'
    
class ReiviewLimitCursorPage(CursorPagination):
    page_size = 3
    ordering ='created'
    