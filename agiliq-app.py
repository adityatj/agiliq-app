import urllib2, urllib, json

get_data = {}

get_data['client_id'] = 'szZwr7btCFclzzMZJI07zzevkvdPj27Eumzrc5KT3hOrzPZuqp'
get_data['redirect_uri'] = 'http://localhost/callback'
get_data['client_secret'] = 'xv8QwDHEZjb9b5lKhZ0teSCauaifbXFeY3Yi9USj1OfzCGCBo6'
get_data['code'] = 'r3VXJuBydK2Fso9VberHshO6Jp7yn4ypZmrXYmNVDDOKwmv7yO' #herpderp

payload = urllib.urlencode(get_data)
print payload

req = urllib2.Request('http://join.agiliq.com/oauth/access_token/?' + payload)
res = urllib2.urlopen(req)

json_data = json.loads(res.readline().strip())

print json_data['access_token']
