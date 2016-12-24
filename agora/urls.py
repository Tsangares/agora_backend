from django.conf.urls import url, include
from django.contrib import admin
from bin.views import *
from django.contrib.auth.models import User
from tastypie.api import Api
from bin.resources import *
from bin.resources_min import *
from django.contrib.auth import views as auth_views

full_api = Api(api_name='full')
full_api.register(AgoraUserResourse())
full_api.register(QuestionResourse())
full_api.register(ResponseResourse())
full_api.register(VoteResource())
full_api.register(RegisterResource())
full_api.register(ModuleResource())
full_api.register(CommentResource())
full_api.register(LoginResource())
full_api.register(TagResource())
min_api = Api(api_name='min')
min_api.register(AgoraUserResourse_min())
min_api.register(QuestionResourse_min())
min_api.register(ResponseResourse_min())
min_api.register(VoteResource_min())
min_api.register(ModuleResource_min())
min_api.register(CommentResource_min())
min_api.register(TagResource_min())
min_api.register(LoginResource())
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(full_api.urls)),
    url(r'^', include(min_api.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^doc/$', doc),
    url(r'^chart$', chart),
    url(r'^chart/new$', chartnew),
]
