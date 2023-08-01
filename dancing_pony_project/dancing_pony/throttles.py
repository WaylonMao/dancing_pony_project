from rest_framework.throttling import SimpleRateThrottle


class DishesRateThrottle(SimpleRateThrottle):
    scope = 'dishes'

    def get_cache_key(self, request, view):
        return self.get_ident(request)
