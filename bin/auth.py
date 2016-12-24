from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.exceptions import Unauthorized
class AgoraAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == "GET":
            return True
        else:
            return super(AgoraAuthentication, self).is_authenticated(request, **kwargs)
class AgoraAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list

    def read_detail(self, object_list, bundle):
        return True

    def create_list(self, object_list, bundle):
        raise Unauthorized("Sorry, too much.")

    def create_detail(self, object_list, bundle):
        return True;

    def update_list(self, object_list, bundle):
        return object_list

    def update_detail(self, object_list, bundle):
        return True

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
