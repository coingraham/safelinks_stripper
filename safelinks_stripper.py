import urllib


def strip(url):

    original_url = url.split("?url=")[1]

    return urllib.unquote(original_url).decode('utf8')


if __name__ == '__main__':
    my_url = "https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsns.us-east-1.amazonaws.com%2Funsubscribe.html%3FSubscriptionArn%3Darn%3Aaws%3Asns%3Aus-east-1%3A699413969599%3Aautomation-topic-cgraham%3A3c7321f7-ed2e-4304-b0a3-c27d0b53656a%26Endpoint%3Dcgraham%402ndwatch.com&amp;data=02%7C01%7Ccgraham%402ndwatch.com%7C9fd67da8bf4c45c7a2f008d685911ad7%7C8242a0a9c4154206be3906637ad2817a%7C0%7C0%7C636843255603819792&amp;sdata=qPXA1iap%2FEy%2Fei1f7dWl6o6q9OmE7iILN2XZvQ0Gaa4%3D&amp;reserved=0"

    print strip(url=my_url)
