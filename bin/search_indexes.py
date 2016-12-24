import datetime
from haystack import indexes
from bin.models import *


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True,model_attr='text')
    #response_text = indexes.CharField(model_attr='responses')
    #response_text = indexes.CharField()
    #def prepare_response_text(self, obj):
    #    return ', '.join([r.response_text for r in obj.responses.all()])
    def get_model(self):
        return Question

class ResponseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True,model_attr='text')
    def get_model(self):
        return Response
class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    user__username = indexes.CharField(model_attr='user__username')
    def get_model(self):
        return AgoraUser
