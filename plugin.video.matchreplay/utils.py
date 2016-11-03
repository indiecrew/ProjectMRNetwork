import urllib, urllib2, re, cookielib, os.path, sys
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, sqlite3, urlresolver

from jsunpack import unpack

from StringIO import StringIO
import gzip

__scriptname__ = "match replay"
__author__ = "indiecrew"
__scriptid__ = "plugin.video.matchreplay"
__credits__ = "mortael"
__version__ = "0.0.3"

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}

addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon(id=__scriptid__)

progress = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()

rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)
resDir = os.path.join(rootDir, 'resources')
imgDir = os.path.join(resDir, 'images')
umicon = xbmc.translatePath(os.path.join(rootDir, 'icon.png'))

profileDir = addon.getAddonInfo('profile')
profileDir = xbmc.translatePath(profileDir).decode("utf-8")
cookiePath = os.path.join(profileDir, 'cookies.lwp')

if not os.path.exists(profileDir):
    os.makedirs(profileDir)

urlopen = urllib2.urlopen
cj = cookielib.LWPCookieJar()
Request = urllib2.Request

if cj != None:
    if os.path.isfile(xbmc.translatePath(cookiePath)):
        try:
            cj.load(xbmc.translatePath(cookiePath))
        except:
            try:
                os.remove(xbmc.translatePath(cookiePath))
                pass
            except:
                dialog.ok('Oh no','The Cookie file is locked, please restart Kodi')
                pass
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
else:
    opener = urllib2.build_opener()

urllib2.install_opener(opener)

favoritesdb = os.path.join(profileDir, 'favorites.db')


def getHtml(url, referer='', hdr=None, NoCookie=None, data=None):
    if not hdr:
        req = Request(url, data, headers)
    else:
        req = Request(url, data, hdr)
    if len(referer) > 1:
        req.add_header('Referer', referer)
    if data:
        req.add_header('Content-Length', len(data))
    response = urlopen(req, timeout=60)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO( response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        f.close()
    else:
        data = response.read()    
    if not NoCookie:
        # Cope with problematic timestamp values on RPi on OpenElec 4.2.1
        try:
            cj.save(cookiePath)
        except: pass
    response.close()
    return data


def getHtml2(url):
    req = Request(url)
    response = urlopen(req, timeout=60)
    data = response.read()
    response.close()
    return data 


def getVideoLink(url, referer):
    req2 = Request(url, '', headers)
    req2.add_header('Referer', referer)
    url2 = urlopen(req2).geturl()
    return url2


def PLAYVIDEO(url, name):
    progress.create('Play video', 'Searching videofile')
    progress.update( 10, "", "Loading video page", "" )
    videosource = getHtml(url, url)
    playvideo(videosource, name, url)


def playvideo(videosource, name, url=None):
    hosts = []
    if re.search('config.playwire.com', videosource, re.DOTALL | re.IGNORECASE):
        hosts.append('Playwire')
    if re.search('youtube.com', videosource, re.DOTALL | re.IGNORECASE):
        hosts.append('Youtube')
    if re.search('mail.ru', videosource, re.DOTALL | re.IGNORECASE):
        hosts.append('Mail')
    if re.search('openload\.(?:co|io)?/', videosource, re.DOTALL | re.IGNORECASE):
        hosts.append('OpenLoad')
    if len(hosts) == 0:
        progress.close()
        dialog.ok('Oh no','Couldn\'t find any playable video')
        return
    elif len(hosts) > 1:
        if addon.getSetting("dontask") == "true":
            vidhost = hosts[0]            
        else:
            vh = dialog.select('Videohost:', hosts)
            vidhost = hosts[vh]
    else:
        vidhost = hosts[0]
    
    if vidhost == 'Playwire':
        progress.update( 40, "", "Loading Playwire", "" )
        playwireurl = re.compile(r'config\.playwire\.com/([^"]+)/zeus\.json', re.DOTALL | re.IGNORECASE).findall(videosource)
        playwireurl = chkmultivids(playwireurl)
        playwireurl = 'https://config.playwire.com/%s/manifest.f4m' % playwireurl
        progress.update( 60, "", "Loading Playwire", "Getting video file from Playwire" )
        playwiresrc = getHtml2(playwireurl)
        videourl = re.compile('<baseURL>([^<]+)</baseURL>', re.DOTALL | re.IGNORECASE).findall(playwiresrc)
        videohash = re.compile('media url="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(playwiresrc)
        progress.update( 80, "", "Loading Playwire", "Found the video" )
        videourl = videourl[0] + "/" + videohash[0]
    elif vidhost == 'Youtube':
        progress.update( 40, "", "Loading Youtube", "" )
        youtubeurl = re.compile("youtube\.com/embed/([^']+)", re.DOTALL | re.IGNORECASE).findall(videosource)
        youtubeurl = chkmultivids(youtubeurl)
        progress.update( 80, "", "Loading Youtube", "Getting video file from Youtube" )
        videourl = "plugin://plugin.video.youtube/?action=play_video&amp;videoid=" + youtubeurl
    elif vidhost == 'Mail':
        progress.update( 40, "", "Loading Mail", "" )
        mailurl = re.compile(r'my\.mail\.ru/video/embed/([^"]+)', re.DOTALL | re.IGNORECASE).findall(videosource)
        mailurl = chkmultivids(mailurl)
        mailurl1 = 'http://videoapi.my.mail.ru/videos/%s.json' % mailurl
        progress.update( 50, "", "Loading Mail", "Sending it to urlresolver" )
        try:
            video = urlresolver.resolve(mailurl1)
            if video:
                progress.update( 80, "", "Loading Mail", "Found the video" )
                videourl = video
        except:
            notify('Oh oh','Couldn\'t find playable Mail link')
            return
    elif vidhost == 'OpenLoad':
        progress.update( 40, "", "Loading Openload", "" )
        openloadurl = re.compile(r"//(?:www\.)?o(?:pen)?load\.(?:co|io)?/(?:embed|f)/([0-9a-zA-Z-_]+)", re.DOTALL | re.IGNORECASE).findall(videosource)
        openloadurl = chkmultivids(openloadurl)
        openloadurl1 = 'http://openload.io/embed/%s/' % openloadurl
        progress.update( 50, "", "Loading Openload", "Sending it to urlresolver" )
        try:
            video = urlresolver.resolve(openloadurl1)
            if video:
                progress.update( 80, "", "Loading Openload", "Found the video" )
                videourl = video
        except:
            notify('Oh oh','Couldn\'t find playable OpenLoad link')
            return

    progress.close()
    playvid(videourl, name)


def playvid(videourl, name):
    iconimage = xbmc.getInfoImage("ListItem.Thumb")
    listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    listitem.setInfo('video', {'Title': name, 'Genre': 'Movies'})
    xbmc.Player().play(videourl, listitem)


def addLink(name, url, mode, iconimage, desc, stream=None, fav='add'):
    contextMenuItems = []
    if fav == 'add': favtext = "Add to"
    elif fav == 'del': favtext = "Remove from"
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    favorite = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&fav=" + fav +
         "&favmode=" + str(mode) +
         "&mode=" + str('900') +
         "&img=" + urllib.quote_plus(iconimage) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    fanart = os.path.join(rootDir, 'fanart.jpg')
    if addon.getSetting('posterfanart') == 'true':
        fanart = iconimage
        liz.setArt({'poster': iconimage})
    liz.setArt({'fanart': fanart})
    if stream:
        liz.setProperty('IsPlayable', 'true')
    if len(desc) < 1:
        liz.setInfo(type="Video", infoLabels={"Title": name})
    else:
        liz.setInfo(type="Video", infoLabels={"Title": name, "plot": desc, "plotoutline": desc})
    contextMenuItems.append(('[COLOR=FFED186A]' + favtext + ' match replay favourites[/COLOR]', 'xbmc.RunPlugin('+favorite+')'))
    liz.addContextMenuItems(contextMenuItems, replaceItems=False)
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=False)
    return ok


def addDir(name, url, mode, iconimage, page=None, channel=None, section=None, keyword='', Folder=True):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&page=" + str(page) +
         "&channel=" + str(channel) +
         "&section=" + str(section) +
         "&keyword=" + urllib.quote_plus(keyword) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    fanart = os.path.join(rootDir, 'fanart.jpg')
    if addon.getSetting('posterfanart') == 'true':
         fanart = iconimage
         liz.setArt({'poster': iconimage})
    liz.setArt({'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=Folder)
    return ok


def _get_keyboard(default="", heading="", hidden=False):
    """ shows a keyboard and returns a value """
    keyboard = xbmc.Keyboard(default, heading, hidden)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return unicode(keyboard.getText(), "utf-8")
    return default  

    
def chkmultivids(videomatch):
    videolist = list(set(videomatch))
    if len(videolist) > 1:
        i = 1
        hashlist = []
        for x in videolist:
            hashlist.append('Video ' + str(i))
            i += 1
        mvideo = dialog.select('Multiple videos found', hashlist)
        return videolist[mvideo]
    else:
        return videomatch[0]


def notify(header=None, msg='', duration=5000):
    if header is None: header = '[COLOR=FFED186A]match replay[/COLOR]'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, umicon)
    xbmc.executebuiltin(builtin)


def cleanname(text):
    text = text.replace(' - ','[COLOR=FFED186A] vs [/COLOR]')
    text = text.replace(' vs ','[COLOR=FFED186A] vs [/COLOR]')
    text = text.replace(' at ','[COLOR=FFED186A] vs [/COLOR]')
    text = text.replace('January','1')
    text = text.replace('Jan','1')
    text = text.replace('February','2')
    text = text.replace('Feb','2')
    text = text.replace('March','3')
    text = text.replace('Mar','3')
    text = text.replace('April','4')
    text = text.replace('Apr','4')
    text = text.replace('May','5')
    text = text.replace('June','6')
    text = text.replace('Jun','6')
    text = text.replace('July','7')
    text = text.replace('Jul','7')
    text = text.replace('August','8')
    text = text.replace('Aug','8')
    text = text.replace('September','9')
    text = text.replace('Sep','9')
    text = text.replace('October','10')
    text = text.replace('Oct','10')
    text = text.replace('November','11')
    text = text.replace('Nov','11')
    text = text.replace('December','12')
    text = text.replace('Dec','12')
    text = text.replace('&','&amp;')
    text = text.replace('&#8211;','-')
    text = text.replace('&#038;','&')
    text = text.replace('&#8217;','\'')
    text = text.replace('&#8216;','\'')
    text = text.replace('&#8230;','...')
    text = text.replace('&quot;','"')
    text = text.replace('&#039;','`')
    text = text.replace('&rsquo;','\'')
    return text


def searchDir(url, mode, page=None):
    conn = sqlite3.connect(favoritesdb)
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM keywords")
        for (keyword,) in c.fetchall():
            name = '[COLOR=FFED186A]' + urllib.unquote_plus(keyword) + '[/COLOR]'
            addDir(name, url, mode, '', page=page, keyword=keyword)
    except: pass
    addDir('[COLOR=FFED186A]Add Keyword[/COLOR]', url, 902, '', '', mode, Folder=False)
    addDir('[COLOR=FFED186A]Clear list[/COLOR]', '', 903, '', Folder=False)
    xbmcplugin.endOfDirectory(addon_handle)


def newSearch(url, mode):
    vq = _get_keyboard(heading="Searching for...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    addKeyword(title)
    xbmc.executebuiltin('Container.Refresh')


def clearSearch():
    delKeyword()
    xbmc.executebuiltin('Container.Refresh')


def addKeyword(keyword):
    xbmc.log(keyword)
    conn = sqlite3.connect(favoritesdb)
    c = conn.cursor()
    c.execute("INSERT INTO keywords VALUES (?)", (keyword,))
    conn.commit()
    conn.close()


def delKeyword():
    conn = sqlite3.connect(favoritesdb)
    c = conn.cursor()
    c.execute("DELETE FROM keywords;")
    conn.commit()
    conn.close()