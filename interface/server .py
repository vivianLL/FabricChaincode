import BaseHTTPServer
import urllib
import time
import json
import subprocess
import re

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	
	def getResult(self):
		print ("resultget")
		with open("result",'r') as fp:
			st = fp.read()
			st = st.split("\n")
			str = st[-3].replace("\\","")
			r = re.findall('{".*}',str)
			print("resutl"+r[0])
			if  r[0]:
				 return r[0] 
			else:
				 return '{"result": 0,"error_code": 0,"error_msg": "error"}'		
	
		
	def do_POST(self):
		path = self.path
		datas = self.rfile.read(int(self.headers['content-length']))
		datas = urllib.unquote(datas).decode("utf-8",'ignore')
		
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.send_header("test","This is test!")
		self.end_headers()
		#print(datas)
		
		datas = json.loads(datas)
		print datas
		operation = datas["operation"]
		del datas["operation"]
		cmd = ''' peer chaincode invoke -o orderer.example.com:7050  --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -n mycc -V 3.0 -c '{"Args":["'''  + operation + '","'
		cmd = cmd + json.dumps(datas).replace(r'"',r'\"') + ''' "]}'  -C mychannel  > result 2>&1''' 	
		print cmd
		try:
			subprocess.check_output(cmd,shell=True)
			result = self.getResult()
		except:
			result = '{"result": 0,"error_code": 0,"error_msg": "error"}'
		print("resultis :"+result)
		self.wfile.write(result)

if __name__ == '__main__':
	serverAddress = ('',8080)
	server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
	server.serve_forever()


