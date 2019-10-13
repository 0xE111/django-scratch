from django.utils.cache import patch_vary_headers


class VaryXRequestedWithMiddleware:
    """ Middleware which adds `Vary:X-Requested-With` header to each response """
    def __init__(self, get_response: callable):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        patch_vary_headers(response, newheaders=['X-Requested-With'])
        return response
