

########### Python 2 #############
import httplib as httplib, urllib as urllib, base64
import json
"""
body = {"URL": "http://i.telegraph.co.uk/multimedia/archive/03442/DEBATE_FIRST_PIC_3442872k.jpg" }

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '4211f4e020b74e23b73be45672d4f2c7',
}

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize", json.dumps(body) , headers)
    response = conn.getresponse()#
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print (e)
    # print("[Errno {0}] {1}".format(e.errno, e.strerror))
"""

class VisionAPI:
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '4211f4e020b74e23b73be45672d4f2c7',
    }

    body = {"URL": None}

    def __init__(self):
        pass

    def get_json(self, url):
        self.body["URL"] = url
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize", json.dumps(self.body) , self.headers)
        response = conn.getresponse()#
        data = response.read()
        # print(data)
        conn.close()
        return data

if __name__ == "__main__":
    test = VisionAPI()
    print test.get_json("http://i.telegraph.co.uk/multimedia/archive/03442/DEBATE_FIRST_PIC_3442872k.jpg")
