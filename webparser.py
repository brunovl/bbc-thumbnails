def images(urls, res, namearg):
    imgurl = []
    names = []
    import urllib.request
    from bs4 import BeautifulSoup
    namerror = False
    for x in urls:
        opener = urllib.request.build_opener()
        urllib.request.install_opener(opener)
        soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'lxml')
        imgs = soup.findAll("img", {"src": True})
        resrep = imgs[1]["src"].split("/")[-2]
        imgurl.append(imgs[1]["src"].replace(resrep, res))
        try:
            if namearg:
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
        except IndexError as error:
            namerror = error
    return imgurl, names, namerror


def series(seriesurl, res, namearg):
    import urllib.request
    from bs4 import BeautifulSoup
    urls = []
    names = []
    opener = urllib.request.build_opener()
    urllib.request.install_opener(opener)
    soup = BeautifulSoup(urllib.request.urlopen(seriesurl).read(), 'lxml')
    divs = soup.findAll("div", {"class": "programme__img-box"})
    for x in divs:
        y = x.contents
        resrep = y[1]["data-src"].split("/")[-2]
        urls.append(y[1]["data-src"].replace(resrep, res))
    if namearg:
        for x in range(len(urls)):
            episode = soup.findAll("span", {"class": "programme__title gamma"})
            series = soup.findAll("a", {"class": "context__item"})
            number = soup.findAll("abbr", {"title": True})
            try:
                if 'Episode' in number[x]["title"]:
                    name = [series[0].text, series[1].text, number[x]["title"], episode[x].contents[0].text]
            except:
                name = [series[0].text, series[1].text, '', episode[x].contents[0].text]
            names.append(name)
    return urls, names
