import fire, json
import http.client, urllib.request, urllib.parse, urllib.error, base64
 
class FacePI:
    def readConfig(self):
        with open('Config.json','r',encoding='utf-8') as f:
            config =json.load(f)
        return config
    def writeConfig(self,config):
        with open('Config.json','w',encoding='utf-8') as f:
            json.dump(config,f)
    def setConfig(self):
        config =self.readConfig()
        print('[]號為預設值,按ENTER表示不更動')
        api_key=input(f'輸入有效的API_KEY[{["api_key"]}]:')
        if api_key: config['api_key'] = api_key
        title =input(f'輸入title[{config["title"]}]:')
        if title: config['title']=title
        self.writeConfig(config)
 
    def test(self):
        print(self.readConfig())
        config = self.readConfig()
        print(config['title'])
 
 
if __name__ == '__main__':
    fire.Fire(FacePI)
 
def detectImageUrl(self,imageurl):
 
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': self.readConfig()['api_key'],
    }
 
    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender',
        #'recognitionModel': 'recognition_04',
        'returnRecognitionModel': 'false',
        'detectionModel': 'detection_01',
        'faceIdTimeToLive': '86400',
    })
    print('imageurl=',imageurl)
    requestbody = '{"url":"'+ imageurl+' ''}'
    try:
        conn = http.client.HTTPSConnection( self.readConfig()['host'])
        conn.request("POST", "/face/v1.0/detect?%s" % params, requestbody, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    
        print("detectLocalImage:",f"{imageurl} 偵測到 {len(json_face_detect)} 個人")
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
 
 
