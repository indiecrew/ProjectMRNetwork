import urllib, urllib2, re, cookielib, os.path, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils


def Main():
    utils.addDir('[COLOR=FFED186A]National Football League[/COLOR] | [COLOR white]USA[/COLOR]','','',os.path.join(utils.imgDir, 'nfl.png'),'')
    List('http://fullmatchtv.com/category/americanfootball/page/1')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    try:
        listhtml = utils.getHtml(url, '')
    except:
        utils.notify('Oh no','It looks like this website is under maintenance')
        return None
    match = re.compile('<div class="td-category-grid">(.*?)<div class="td-pb-span4', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
    match1 = re.compile(r'class="td-module-thumb"><a href="([^"]+)".*?src="([^"]+)" alt="([^"]+)".*?<time class=".*?" datetime=".*?" >([^"]+) ([^"]+), ([^"]+)</time>', re.DOTALL | re.IGNORECASE).findall(match)
    for videopage, img, name, month, day, year in match1:
        month = utils.cleanname(month)
        date = '%s/%s/%s'%(month,day,year) 
        name = utils.cleanname(name)
        name = '%s %s'%(date, name)
        utils.addLink(name, videopage, 62, img, '')
    try:
        nextp=re.compile('<link rel="next" href="([^"]+)" />', re.DOTALL | re.IGNORECASE).findall(listhtml)
        utils.addDir('[COLOR=FFED186A]Next Page[/COLOR]', nextp[0], 61,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Playvid(url, name):
    utils.PLAYVIDEO(url, name)
