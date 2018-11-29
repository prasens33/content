import requests
import json
import time

HOST = "https://10.0.1.248"
restAddress = HOST + "/phoenix/rest/h5/report"
USERNAME = 'admin'
PASSWORD = 'CorSIEMDubai@Lab2018'
VERIFY_SSL = False
URL = HOST + "/phoenix/rest/query/"
VIEW_STATE = '5OeE5cIQWBhQa91ot4ZxebVyFdSw6l4XJ0hkynw7ZRhJV87aZMHp53fhYIlAO5o08kL8bBNj1YahD2zmJMSZxLI5GKg7M10UVfrDijY9xv3aS3o8bxQtePaVPTERgw7xJQZ5m+G/j2Ht7agGCIJ6YZVQ70XoG8O0GOsOk2xZSPFwMzstxi4ebZQ3B+6/HWJ9E5n8Ttfs4ZCa+0723vqyI+P/LPEetKkKbD8yqA9oY7jysrJqdCQgqwfETKdrUqyvWHgL7N9bEfNe5AkrfdtzMnRwk+qUxvkO0FlXi7heozqFEQ2wYiGxKGPR+kXLh1RN/RksbntoPreDSeFiCOfAH4qL9dJ+M0IuL1nOeom8WYZsWroSzU/4nTGbvwqj2sR2yzWKHC8BUapeYwLD4OSGaUoY+uSKkZrmtcsj1ulXe9UV4Z7jHt3AvzyNjhQgyLA0CdLSIZ7WBJNqm1XsERfmpZRSg9v45ZUwJ5VW+1agCRyGOEJZ05MOevzlwBEIast2PcoozyTg99jP4kPUBbLp0RXLYK+zO7fCJHX7Bh1qWgUOy/1D3DN2TtDAyAonzaId/zVe+A9S4DniuFOSMA3EZGfNCcWzSer8uclVfBEMsqS6fwdt3thx21DJDnFjAILIb4dzbEjpTigoZy66SabJdZqNZXY7y+mpgLpgVn8V4Nk9daSTteYVrCdgyV5dMbDSkasLrLBIrvg8kTlJghuP951Ab0U+SsO+mX80C0SXw+8PIodHzZW/QSTqDX2vEfVHh949PKCasey+f4vRv2ZCgDhsT5qzDzdJvkFOtqjk8FKK4eRlgPUWAueaR2JMwQW0TRh1ZOYWoRuzy5LgMI9kMKRh9j/PuWU3KBNM+GHh5FSgc0SCaDUqnP2LpDXNd9yV0X8iK3Z0Lte5MWOtmQQwMBqci9353TD7fv6nCbzXXvti4DCMid8IrAcqs0bibyYP9+RjMd++8ow6HwVVwfTDK/G7b8otXzIHLcSnNJft0YoaD7Y6r80ebahsxqPWMhHvpl9ZWRzhH6e83rud/VW0NQ=='
requests.packages.urllib3.disable_warnings()

def validateSuccessfulResponse(resp):
    if resp.status_code != 200:
        # demisto.results(errorEntry("Got response status " + str(resp.status_code) + " when fetching event query"))
        print "error!!!! " + resp.text
        exit(0)


def getIncidentEvents():
    fortiIncID = "111"
    max_events = "30"
    extendedData = "true"

    session=requests.session()

    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,he;q=0.8'
    }
    data = {
      'loginHtml': 'loginHtml',
      'loginHtml:username': USERNAME,
      'loginHtml:password': PASSWORD,
      'loginHtml:userDomain': 'Empty',
      'loginHtml:loginBtn': 'Log In',
      'javax.faces.ViewState': VIEW_STATE
    }

    response = session.post('https://10.0.1.248/phoenix/login-html.jsf', headers=headers, data=data, verify=False)
    response = session.get('https://10.0.1.248/phoenix/rest/h5/report/triggerEvent?rawMsg='+fortiIncID)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    try:
        jsonRes = response.json()
        if (type(jsonRes) is not list) or (len(jsonRes) <= 0) or (jsonRes[0].get('right', None) is None):
            # demisto.results(errorEntry("Got response status " + str(resp.status_code) + " when fetching event query"))
            raise "error!!!! " + response.text
    except Exception as err:
        # demisto.results(errorEntry("Got response status " + str(resp.status_code) + " when fetching event query"))
        print "some error " + str(err)
        exit(0)

    queryData = jsonRes[0]['right']
    response = session.post(restAddress + '/run', headers=headers, data=json.dumps(queryData), verify=False )
    validateSuccessfulResponse(response)

    data = response.text
    while response.text != "100":
        response = session.post(restAddress+'/reportProgress', headers=headers, data=data, verify=False)
        time.sleep(1)

    data = json.loads(data)
    print data
    data["report"] = queryData
    data = json.dumps(data)
    response = session.post(restAddress+'/resultByReport?start=0&perPage='+max_events+'&allData='+extendedData, headers=headers, data=data, verify=False)

    try:
        res = response.json()
        eventKeys = res["headerData"]["columnNames"]
    except Exception as err:
        # demisto.results(errorEntry("Got response status " + str(resp.status_code) + " when fetching event query"))
        print "some error " + str(err) + res.text
        exit(0)

    # res = response.json()
    # eventKeys = res["headerData"]["columnNames"]
    eventData = []

    for key in res["lightValueObjects"]:
        cur = {}
        for i in range(0, len(eventKeys)):
            cur[eventKeys[i]] = key["data"][i]
        cur["extendedData"] = {}
        for extItem in key["extData"]:
            cur["extendedData"][extItem["left"]] = extItem["right"]
        eventData.append(cur)

    print json.dumps(eventData)

getIncidentEvents()