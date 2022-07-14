from django.urls import  include,re_path
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
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(full_api.urls)),
    re_path(r'^', include(min_api.urls)),
    re_path(r'^search/', include('haystack.urls')),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    re_path(r'^doc/$', doc),
    re_path(r'^chart$', chart),
    re_path(r'^chart/new$', chartnew),
]
