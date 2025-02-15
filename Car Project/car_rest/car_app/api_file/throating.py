from rest_framework.throttling import UserRateThrottle

class ReiviewDetailThrottle(UserRateThrottle):
    scope ='reiview_detail_throttle'
    

class ReiviewListThrottle(UserRateThrottle):
    scope ='reiview_list_throttle'