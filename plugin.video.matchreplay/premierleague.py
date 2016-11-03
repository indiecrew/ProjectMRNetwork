import urllib, urllib2, re, cookielib, os.path, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils


def Main():
    utils.addDir('[COLOR=FFED186A]Premier League[/COLOR] | [COLOR white]England[/COLOR]','','',os.path.join(utils.imgDir, 'PremierLeague.png'),'')
    List('http://www.socceryou.com/en/full-matches.php?competition=1')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    try:
        listhtml = utils.getHtml(url, '')
    except:
        utils.notify('Oh no','It looks like this website is under maintenance')
        return None
    match = re.compile('<div id="pagination">(.*?)<div id="bet-ban-r1">', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
    match1 = re.compile(r'class="footer-sx".*?alt="England - Premier League">.*? - .*? - (.+?)/(.+?)/(.+?)</a>.*?class="foto-video".*?href="([^"]+)">.*?<img src="([^"]+)".*?<h3>(.+?)</h3>', re.DOTALL | re.IGNORECASE).findall(match)
    for day, month, year, videopage, img, name in match1:
        date = '%s/%s/%s'%(month,day,year)  
        name = utils.cleanname(name)
        name = '%s %s'%(date, name)
	videopage = 'http://www.socceryou.com/en/%s'%(videopage)
        utils.addLink(name, videopage, 15, img, '')
    try:
        nextp = re.compile(r'<a href="([^"]+)">Next</a>', re.DOTALL | re.IGNORECASE).findall(match)
        utils.addDir('[COLOR=FFED186A]Next Page[/COLOR]', 'http://www.socceryou.com/en/full-matches.php' + nextp, 11,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List2(url, name):
    listhtml = utils.getHtml(url, '')
    match = re.split("class='video_button'><a class='btn2 filter' href='([^']+)'>(.+?)</a>").findall(listhtml)
    for url, name in match:
        utils.addLink(name, 'http://www.socceryou.com/en/' + url, 12, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Playvid(url, name):
    utils.PLAYVIDEO(url, name)
