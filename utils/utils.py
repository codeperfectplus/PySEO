import re


def get_all_urls(text, exclude_keywords=[".js, .css"]):
    """ Get all the urls from the text
    
    Args:
        text (str): text to extract urls from
    
    Returns:
        list: list of urls
    """
    urls_list = []
    urls = re.findall(r'(https?://\S+)', text)
    
    # remove urls if exclude_keywords are present in the url using list comprehension
    urls = [url for url in urls if not any(keyword in url for keyword in exclude_keywords)]
    return urls




if __name__ == '__main__':
    path = 'sample/test.html'
    with open(path, 'r') as f:
        text = f.read()
    urls = get_all_urls(text)
    print(urls)