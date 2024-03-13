import resquests
reponse = resquests.get('http://www.google.com')
print (reponse.status_code)
