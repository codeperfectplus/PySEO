import requests


def ping(url):
    """ Ping the url and return True if status code is 200
     
    Args:
        url (str): url to ping
    
    Returns:
        bool: True if status code is 200 else False
    """
    status_code = requests.get(url).status_code
    if status_code == 200:
        return True
    return False

class Crawler:
    """ Crawler class to crawl the url and return the response
     
    Functions:
        get: get the response of the url
        post: post the data to the url and return the response
        get_json: get the json response of the url

    Args:
        url (str): url to crawl

    Returns:
        str: response of the url
    """

    def __init__(self, url):
        self.url = url

    def get(self):
        with requests.Session() as session:
            return session.get(self.url).text

    def post(self, data):
        with requests.Session() as session:
            return session.post(self.url, data=data).text
    
    def get_json(self):
        with requests.Session() as session:
            return session.get(self.url).json()
        

def test_case():
    crawler = Crawler('https://www.wheretogo.co.in')
    data = crawler.get()

    with open('sample/test.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    test_case()