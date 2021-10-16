from rest_framework.authentication import BaseAuthentication, get_authorization_header


class UserFaker:
    is_authenticated = True


class CustomTokenAuthentication(BaseAuthentication):
    keyword = "Token"

    def authenticate(self, request):
        auth = get_authorization_header(request)
        if not request.META.get("HTTP_AUTHORIZATION", b""):
            return None

        code = auth.decode("utf-8").split(" ")[1]

        if not code.lower().startswith("puc"):
            return None

        return (UserFaker(), "None")

    def authenticate_header(self, request):
        return self.keyword
