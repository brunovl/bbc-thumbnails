def images(urls, res):
    imgurl = []
    import urllib.request
    from bs4 import BeautifulSoup
    for x in urls:
        opener = urllib.request.build_opener()
        urllib.request.install_opener(opener)
        soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'html.parser')
        imgs = soup.findAll("img", {"src": True})
        resrep = imgs[1]["src"].split("/")[-2]
        imgurl.append(imgs[1]["src"].replace(resrep, res))
    return imgurl


def names(urls):
    import urllib.request
    from bs4 import BeautifulSoup
    names = []
    for x in urls:
        opener = urllib.request.build_opener()
        urllib.request.install_opener(opener)
        soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'html.parser')
        episode = soup.findAll("h1", {"class": "no-margin"})
        series = soup.findAll("a", {"class": "context__item"})
        number = soup.findAll("span")
        if 'Episode' in number[6].text.strip():
            name = [series[0].text, series[1].text, number[6].text.strip(), episode[0].text]
        elif 'Episode' in number[4].text.strip():
            name = [series[0].text, series[1].text, number[4].text.strip(), episode[0].text]
        else:
            name = [series[0].text, series[1].text, '', episode[0].text]
        names.append(name)
    return names


def series(seriesurl):
    import urllib.request
    from bs4 import BeautifulSoup
    urls = []
    opener = urllib.request.build_opener()
    urllib.request.install_opener(opener)
    soup = BeautifulSoup(urllib.request.urlopen(seriesurl).read(), 'html.parser')
    links = soup.findAll("a", {"class": "br-blocklink__link block-link__target", "href": True})
    for x in links:
        urls.append(x['href'])
    return urls
