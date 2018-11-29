import requests
from dateutil.parser import parse
 
 
def getResponse(url):
    response = requests.get(url)
    jsonResponse = response.json()
    return jsonResponse
 
 
def getAngularCommitActivity():
    url = "https://a...content-available-to-author-only...b.com/repos/angular/angular.js/stats/commit_activity"
    jsonResponse = getResponse(url)
    print "week_number	total_weekly_commits  dayofWeekCommit"
    for eachActivity in jsonResponse:
        print str(eachActivity['week']) + '        ' + str(eachActivity['total']) + '                ' + str(
            eachActivity['days'])
 
    return
 
 
def getAngularContributors():
    url = "https://a...content-available-to-author-only...b.com/repos/angular/angular.js/stats/contributors"
    jsonResponse = getResponse(url)
    listOfAngularContributors = []
    for a in jsonResponse:
        listOfAngularContributors.append([a['author']['login'], a['total']])
 
    sorted(listOfAngularContributors, key=getSecond, reverse=True)
    print "Top 5 contributors in this project are: "
    for i in range(0, 5):
        a = listOfAngularContributors[i]
        print a[0] + "\t" + str(a[1])
 
    print "Total no of contributors are :", listOfAngularContributors.__sizeof__()
    return
 
 
def getSecond(self):
    return self[1]
 
 
def getAvgBugLifeTimeForAngular():
    url = "https://a...content-available-to-author-only...b.com/repos/angular/angular.js/issues?state=all"
    jsonResponse = getResponse(url)
    totalTime = 0
    count = 0
    for jsonObj in jsonResponse:
        if (jsonObj['state'] == 'closed'):
            count += 1
            close_time = parse(jsonObj['closed_at'])
            open_time = parse(jsonObj['created_at'])
            totalTime += (close_time - open_time).seconds
 
    avgTimeTaken = 0
    if (count != 0):
        avgTimeTaken = float(float(totalTime / count) / 60)
        print ("Average Bug life time for Angular js is: " + str(avgTimeTaken) + " minutes")
 
 
def getBootstrapCommitActivity():
    url = "https://a...content-available-to-author-only...b.com/repos/twbs/bootstrap/stats/commit_activity"
    jsonResponse = getResponse(url)
    print "week_number	total_weekly_commits  dayofWeekCommit"
    for eachActivity in jsonResponse:
        print str(eachActivity['week']) + '        ' + str(eachActivity['total']) + '                ' + str(
            eachActivity['days'])
 
    return
 
 
def getBootstrapContributors():
    url = "https://a...content-available-to-author-only...b.com/repos/twbs/bootstrap/stats/contributors"
    jsonResponse = getResponse(url)
    listOfBootstrapContributors = []
    for a in jsonResponse:
        listOfBootstrapContributors.append([a['author']['login'], a['total']])
 
    sorted(listOfBootstrapContributors, key=getSecond, reverse=True)
    print "Top 5 contributors in this project are: "
    for i in range(0, 5):
        a = listOfBootstrapContributors[i]
        print a[0] + "\t" + str(a[1])
 
    print "Total no of contributors are :", listOfBootstrapContributors.__sizeof__()
    return
 
 
def getAvgBugLifeTimeForBootstrap():
    url = "https://a...content-available-to-author-only...b.com/repos/twbs/bootstrap/issues?state=all"
    jsonResponse = getResponse(url)
    totalTime = 0
    count = 0
    for jsonObj in jsonResponse:
        if (jsonObj['state'] == 'closed'):
            count += 1
            close_time = parse(jsonObj['closed_at'])
            open_time = parse(jsonObj['created_at'])
            totalTime += (close_time - open_time).seconds
 
    avgTimeTaken = 0
    if (count != 0):
        avgTimeTaken = float(float(totalTime / count) / 60)
        print ("Average Bug life time for Angular js is: " + str(avgTimeTaken) + " minutes")
 
def getAngularTopicCountFromStackExchange():
    urlArray = [ "https://a...content-available-to-author-only...e.com/2.2/tags/angularjs/info?order=desc&sort=popular&site=stackoverflow",
        "https://a...content-available-to-author-only...e.com/2.2/tags/angularjs-directive/info?order=desc&sort=popular&site=stackoverflow",
        "https://a...content-available-to-author-only...e.com/2.2/tags/angularjs-scope/info?order=desc&sort=popular&site=stackoverflow"
    ]
    totalPosts = 0 
    for url in urlArray:
        jsonResponse = getResponse(url)
        totalPosts += jsonResponse['items'][0]['count']
    print ("Number of Posts related to angular js on Stack Overflow are : " + str(totalPosts))
 
 
def getBootstrapTopicCountFromStackExchange():
    urlArray = ["https://a...content-available-to-author-only...e.com/2.2/tags/bootstrap-4/info?order=desc&sort=popular&site=stackoverflow",
        "https://a...content-available-to-author-only...e.com/2.2/tags/angular-bootstrap/info?order=desc&sort=popular&site=stackoverflow",
        "https://a...content-available-to-author-only...e.com/2.2/tags/ng-bootstrap/info?order=desc&sort=popular&site=stackoverflow",
        "https://a...content-available-to-author-only...e.com/2.2/tags/twitter-bootstrap/info?order=desc&sort=popular&site=stackoverflow"]
    totalPosts = 0
    for url in urlArray:
        jsonResponse = getResponse(url)
        totalPosts += jsonResponse['items'][0]['count']
    print ("Number of Posts related to Bootstrap on Stack Overflow are : " + str(totalPosts))
 
def getTotalUnansweredQuestionForAngular():
    count = 1
    totalUnAnsweredQuestions = 0
    while(True):
        url = "https://a...content-available-to-author-only...e.com/2.2/questions/unanswered?page="+str(count)+"&pagesize=100&order=desc&sort=activity&tagged=angularjs&site=stackoverflow"
        jsonResponse = getResponse(url)
        #print jsonResponse['items']
        if not('items' in jsonResponse):
            break
        totalUnAnsweredQuestions += len(jsonResponse['items'])
        print( totalUnAnsweredQuestions)
        count += 1
    print("Total Number of Unanswered questions for AngularJs are: "+ str(totalUnAnsweredQuestions))
 
def getTotalUnansweredQuestionForBootstrap():
    count = 1
    totalUnAnsweredQuestions = 0
    while(True):
        url = "https://a...content-available-to-author-only...e.com/2.2/questions/unanswered?page="+str(count)+"&pagesize=100&order=desc&sort=activity&tagged=twitter-bootstrap&site=stackoverflow"
        jsonResponse = getResponse(url)
        if not('items' in jsonResponse):
            break
        totalUnAnsweredQuestions += len(jsonResponse['items'])
        print( totalUnAnsweredQuestions)
        count += 1
    print("Total Number of Unanswered questions for Bootstrap are: "+ str(totalUnAnsweredQuestions))
 
 
 
print "Reports for Angular"
print "--------------------------------"
#getAngularCommitActivity()
print "--------------------------------"
#getAngularContributors()
print "--------------------------------"
#getAvgBugLifeTimeForAngular()
print "--------------------------------"
#getAngularTopicCountFromStackExchange()
print "--------------------------------"
getTotalUnansweredQuestionForAngular()
print "--------------------------------"
 
 
print "\n\n\n\n\n\n"
print "Reports for Bootstrap"
print "--------------------------------"
#getBootstrapCommitActivity()
print "--------------------------------"
#getBootstrapContributors()
print "--------------------------------"
#getAvgBugLifeTimeForBootstrap()
print "--------------------------------"
#getBootstrapTopicCountFromStackExchange()
print "--------------------------------"
getTotalUnansweredQuestionForBootstrap()
print "--------------------------------"
