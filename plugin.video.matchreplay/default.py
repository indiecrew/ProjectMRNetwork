import urllib, urllib2, re, cookielib, os.path, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, xbmcvfs, utils, favorites

import premierleague, mlb, nba, nfl, nhl, prugby

socket.setdefaulttimeout(60)

xbmcplugin.setContent(utils.addon_handle, 'movies')
addon = xbmcaddon.Addon(id=utils.__scriptid__)

progress = utils.progress
dialog = utils.dialog

imgDir = utils.imgDir
rootDir = utils.rootDir

cachedir = 'special://profile/addon_data/plugin.video.matchreplay/cache'


def INDEX():
    utils.addDir('[COLOR grey]Premier League[/COLOR]','',10,os.path.join(imgDir, 'PremierLeague.png'),'')
    utils.addDir('[COLOR grey]National Football League[/COLOR]','',60,os.path.join(imgDir, 'nfl.png'),'')
    utils.addDir('[COLOR grey]National Basketball Association[/COLOR]','',65,os.path.join(imgDir, 'nba.png'),'')
    utils.addDir('[COLOR grey]Major League Baseball[/COLOR]','',70,os.path.join(imgDir, 'mlb.png'),'')
    utils.addDir('[COLOR grey]National Hockey League[/COLOR]','',75,os.path.join(imgDir, 'nhl.png'),'')
    utils.addDir('[COLOR grey]Premiership Rugby[/COLOR]','',80,os.path.join(imgDir, 'PremiershipRugby.png'),'')
    utils.addDir('[COLOR=900C3F]---[/COLOR]','','',os.path.join(rootDir, 'icon.png'),'')
    utils.addDir('[COLOR grey]Favourites[/COLOR]: [COLOR=FFED186A]My List[/COLOR]','',901,os.path.join(rootDir, 'icon.png'),'')
    utils.addDir('[COLOR grey]Setting[/COLOR]: [COLOR=FFED186A]Personal[/COLOR]','',904,os.path.join(rootDir, 'icon.png'),'')
    utils.addDir('[COLOR grey]Twitter[/COLOR]: [COLOR=FFED186A]@MRNetworkTV[/COLOR]','','',os.path.join(rootDir, 'icon.png'),'')
    xbmcplugin.endOfDirectory(utils.addon_handle)

if 'disclaimer' in sys.argv[0]:
    try:
        f = xbmcvfs.File('special://home/addons/plugin.video.matchreplay/disclaimer.txt')
        text = f.read() ; f.close()
        label = '[COLOR=FFED186A]Disclaimer[/COLOR]'
        id = 10147
        xbmc.executebuiltin('ActivateWindow(%d)' % id)
        xbmc.sleep(100)
        win = xbmcgui.Window(id)
        retry = 50
        while (retry > 0):
            try:
                xbmc.sleep(10)
                win.getControl(1).setLabel(label)
                win.getControl(5).setText(text)
                retry = 0
            except:
                retry -= 1
    except:
        pass

if 'clearcache' in sys.argv[0]:
    dirs, files = xbmcvfs.listdir(cachedir)
    for f in files:
        xbmcvfs.delete(cachedir + f)
    dialog = xbmcgui.Dialog()
    dialog.notification('[COLOR=FFED186A]MatchReplay[/COLOR]', 'Clearing cache...', xbmcgui.NOTIFICATION_INFO, 5000)
    quit()

def Settings():
    addon.openSettings(sys.argv[0])
    sys.exit()

if not addon.getSetting('already_shown') == 'true':
    shown = dialog.yesno('This addon contains copyright material','You may enter only if you agree with our disclaimer', nolabel='Exit', yeslabel='Enter')
    addon.setSetting('already_shown', 'true')

def getParams():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if params[len(params) - 1] == '/':
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


params = getParams()
url = None
name = None
mode = None
img = None
page = 1
fav = None
favmode = None
channel = None
keyword = None


try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass
try: page = int(params["page"])
except: pass
try: img = urllib.unquote_plus(params["img"])
except: pass
try: fav = params["fav"]
except: pass
try: favmode = int(params["favmode"])
except: pass
try: channel = int(params["channel"])
except: pass
try: keyword = urllib.unquote_plus(params["keyword"])
except: pass


if mode is None: INDEX()

elif mode == 10: premierleague.Main()
elif mode == 11: premierleague.List(url)
elif mode == 12: premierleague.Playvid(url, name)
elif mode == 13: premierleague.Table(url)
elif mode == 14: premierleague.Fixture(url)
elif mode == 15: premierleague.List2(url, name)

elif mode == 60: nfl.Main()
elif mode == 61: nfl.List(url)
elif mode == 62: nfl.Playvid(url, name)
elif mode == 63: nfl.Table(url)
elif mode == 64: nfl.Fixture(url)

elif mode == 65: nba.Main()
elif mode == 66: nba.List(url)
elif mode == 67: nba.Playvid(url, name)
elif mode == 68: nba.Table(url)
elif mode == 69: nba.Fixture(url)

elif mode == 70: mlb.Main()
elif mode == 71: mlb.List(url)
elif mode == 72: mlb.Playvid(url, name)
elif mode == 73: mlb.Table(url)
elif mode == 74: mlb.Fixture(url)

elif mode == 75: nhl.Main()
elif mode == 76: nhl.List(url)
elif mode == 77: nhl.Playvid(url, name)
elif mode == 78: nhl.Table(url)
elif mode == 79: nhl.Fixture(url)

elif mode == 80: prugby.Main()
elif mode == 81: prugby.List(url)
elif mode == 82: prugby.Playvid(url, name)
elif mode == 83: prugby.Table(url)
elif mode == 84: prugby.Fixture(url)

elif mode == 900: favorites.Favorites(fav,favmode,name,url,img)
elif mode == 901: favorites.List()
elif mode == 902: utils.newSearch(url, channel)
elif mode == 903: utils.clearSearch()
elif mode == 904: Settings()

xbmcplugin.endOfDirectory(utils.addon_handle)