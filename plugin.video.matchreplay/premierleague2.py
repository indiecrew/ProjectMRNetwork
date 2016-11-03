import urllib, urllib2, re, cookielib, os.path, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils


def Main():
    utils.addDir('[COLOR=FFED186A]Premier League[/COLOR] | [COLOR white]England[/COLOR]','','',os.path.join(utils.imgDir, 'PremierLeague.png'),'')
    utils.addDir('[B]Current League Table[/B]','http://www.livefootball.com/football/england/premier-league/league-table/',13,os.path.join(utils.imgDir, 'PremierLeague.png'),'')
    utils.addDir('[B]Upcoming Matches[/B]','http://www.livefootball.com/football/england/premier-league/fixtures/7-days/',14,os.path.join(utils.imgDir, 'PremierLeague.png'),'')
    List('http://livefootballvideo.com/competitions/premier-league')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def List(url):
    try:
        listhtml = utils.getHtml(url, '')
    except:
        utils.notify('Oh no','It looks like this website is under maintenance')
        return None
    match = re.compile('<div id="maincontent">(.*?)<div class="clear">', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
    match1 = re.compile(r'div class="cover"><a href="([^"]+)" rel="bookmark" title="([^"]+)"><img src="([^"]+)".*?class="postmetadata longdate" rel=".*?">([^"]+)</p>', re.DOTALL | re.IGNORECASE).findall(match)
    for videopage, name, img, date in match1:
        name = utils.cleanname(name)
        name = '%s %s'%(date, name)
        utils.addLink(name, videopage, 12, img, '')
    try:
        nextp=re.compile('<a class="page larger" href="([^"]+)">', re.DOTALL | re.IGNORECASE).findall(match)
        utils.addDir('[COLOR=FFED186A]Next Page[/COLOR]', nextp[0], 11,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    utils.PLAYVIDEO(url, name)

def Table(url):
    try:
        tabhtml = utils.getHtml(url, '')
    except:
        utils.notify('Oh no','It looks like this website is under maintenance')
        return None
    utils.addDir('[COLOR white]League Table[/COLOR] | [COLOR=FFED186A]MatchReplay[/COLOR]','','',os.path.join(utils.imgDir, 'PremierLeague.png'),'')
    match = re.compile('<td class="ltid">(.+?)</td><td class="ltn">(.+?)</td>.*?<td class="ltw">(.+?)</td><td class="ltd">(.+?)</td><td class="ltl">(.+?)</td>.*?<td class="ltp">(.+?)</td>', re.DOTALL | re.IGNORECASE).findall(tabhtml)
    for post, name, win, draw, lost, point in match:
        name = '%s. [COLOR=FFED186A]%s[/COLOR] | %s Wins, %s Draws, %s Losses, %s Points'%(post, name, win, draw, lost, point)
        utils.addDir(name, '', 11,  '')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Fixture(url):
    try:
        fixhtml = utils.getHtml(url, '')
    except:
        utils.notify('Oh no','It looks like this website is under maintenance')
        return None
    utils.addDir('[COLOR white]Upcoming Matches[/COLOR] | [COLOR=FFED186A]MatchReplay[/COLOR]','','',os.path.join(utils.imgDir, 'PremierLeague.png'),'')
    match = re.compile('<dd class="mElStatus">(.+?)</dd><dd class="mElO1">(.+?)</dd>.*?<dd class="mElO2">(.+?)</dd>', re.DOTALL | re.IGNORECASE).findall(fixhtml)
    for time, team1, team2 in match:
        name = '%s [COLOR=FFED186A]%s[/COLOR] vs [COLOR=FFED186A]%s[/COLOR]'%(time, team1, team2)
        utils.addDir(name, '', 11,  '')
    xbmcplugin.endOfDirectory(utils.addon_handle)