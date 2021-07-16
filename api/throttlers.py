from rest_framework.throttling import UserRateThrottle

class PostUserRateThrottle(UserRateThrottle):
    scope = 'post_user'
    def allow_request(self, request, view):
        if request.method == "GET":
            return True
        return super().allow_request(request, view)