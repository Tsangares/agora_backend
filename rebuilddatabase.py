import json
import requests
URL_BASE = 'https://startandselect.com/'
URL_REGISTER = '%sapi/full/register/' % URL_BASE
URL_USER = '%s/api/full/user/' % URL_BASE
URL_DATA = '%s/scripts/DownloadAllQuestions.php' % URL_BASE
URL_QUESTION = '%s/api/full/question/' % URL_BASE
URL_RESPONSE = '%s/api/full/response/' % URL_BASE

def makeUser(username, password):
    mydata = {'username': username, 'password': password}
    myhead = {'Content-Type': 'application/json'}
    return requests.post(URL_REGISTER, data=json.dumps(mydata), headers=myhead).text

def getQuestions():
    return json.loads(requests.get(URL_DATA).text)

def loadData(data, username, apikey):
    _i = 0;
    myhead={'Authorization': 'ApiKey %s:%s' % (username, apikey)}
    for question in data:
        _i += 1
        mydata={'text': question['question']}
        print ('Question %s %s' % (_i, question['question']))
        r = requests.post(URL_QUESTION, data=json.dumps(mydata), headers=myhead)
        print 'RESPONSE %s %s' % (r, r.text)
        for response in question['responses']:
            mydata={'text': response['response'], 'question_id': _i}
            print ('Response %s' % (response['response']))
            r = requests.post(URL_RESPONSE, data=json.dumps(mydata), headers=myhead)
            print 'RESPONSE %s %s %s ' % (r, r.reason, r.text)



def start():
    print('started')
    user='tsangares'
    key=json.loads(makeUser(user, 'ethereum'))['key']
    loadData(getQuestions(), user, key)
start()
