def imgdown(urls, dest, namelist, adddir):
    import urllib.request
    import os
    n = 0
    try:
        os.mkdir(dest + adddir)
    except OSError as exc:
        print('[WARNING] Folder creation error ({}), continuing program.'.format(exc))
    if namelist is not None:
        names = []
        for x in namelist:
            names.append(namelist[n][0] + ' ' + namelist[n][1] + ' - ' + namelist[n][2] + ' ' + namelist[n][3])
            n += 1
    else:
        names = None
    n = 0
    for y in urls:
        opener = urllib.request.build_opener()
        urllib.request.install_opener(opener)
        if names is None:
            filename = os.path.join(dest, adddir + y.split("/")[-1])
        else:
            name = names[n].replace(":", "")
            filename = dest + adddir + name + '.jpg'
        img_data = opener.open(y)
        f = open(filename, "wb")
        f.write(img_data.read())
        f.close()
        n += 1
    return True