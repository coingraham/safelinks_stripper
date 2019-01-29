import urllib


def strip(url):

    original_url = url.split("?url=")[1]

    return urllib.unquote(original_url).decode('utf8')


if __name__ == '__main__':
    my_url = ""

    print strip(url=my_url)
