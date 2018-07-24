#-*- coding:utf-8 -*-

import BaseHTTPServer
import urllib
import time
import subprocess
import base64
import json

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	
	def travalJson(dic_json,encode=True):
			if isinstance(dic_json,dict):
					for key in dic_json:
							print key
							if isinstance(dic_json[key],dict):
									print "_*********___"
									travalJson(dic_json[key],encode)
							if isinstance(dic_json[key],list):
									for item in dic_json[key]:
											if isinstance(item,dict):
													travalJson(item,encode)
							else:
									if key=="path_start" or key == "path_end" or key=="link_start" or key == "link_end":
											print "____"
											if encode == True:
													str = dic_json[key]
													str = str.encode('utf-8')
													str = base64.b64encode(str)
													dic_json[key] = str
											else:
													str = dic_json[key]
													print str
													str = base64.b64decode(str)
													print "dest:"+str
													dic_json[key] = str
			return dic_json

	def do_POST(self):
		path = self.path
		datas = self.rfile.read(int(self.headers['content-length']))
		datas = urllib.unquote(datas).decode("utf-8",'ignore')
		
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.send_header("test","This is test!")
		self.end_headers()
		datas = travalJson(json.loads(datas))
		datas = json.dumps(datas)
		
		cmd = "curl --data ' "+datas +" ' 172.19.0.5:8080"
		print(cmd)
		result = subprocess.check_output(cmd,shell=True)		
		result = result.replace("hist","data_list")
		result = travalJson(json.loads(result),encode=False)
		result = json.dumps(result)
		print("return:"+result)
		self.wfile.write(result)

if __name__ == '__main__':
	serverAddress = ('',8080)
	server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
	server.serve_forever()

