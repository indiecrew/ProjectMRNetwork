# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from xbmcswift2 import Plugin


STRINGS = {
    'page': 30001,
    'streams': 30100,
    'streams2': 30101,

}

STATIC_STREAMS = (
    {
        'title': '[COLOR orange]Siaran Langsung dari Makkah dan Madinah[/COLOR]',
        'logo': 'islamicstreamstv.png',
        'stream_url': ('.'),
    },
	{
        'title': 'Masjid al-Haram, Makkah',
        'logo': 'makkah.jpg',
        'stream_url': ('plugin://plugin.video.youtube/play/?video_id=ArVmnth5jB4'),
    },
	{
        'title': 'Al-Masjid an-Nabawi, Madinah',
        'logo': 'madinah.jpg',
        'stream_url': ('plugin://plugin.video.youtube/play/?video_id=4OoKpZWJASY'),
    },
	{
        'title': '[COLOR orange]Islamic TV[/COLOR]',
        'logo': 'islamicstreamstv.png',
        'stream_url': ('.'),
    },
	{
        'title': 'Al-Hijrah (Malaysia)',
        'logo': 'livetv.jpg',
        'stream_url': ('http://d2f9tqsihrp4sc.cloudfront.net/livecf/smil:tvah_hypptv.smil/playlist.m3u8'),
    },
	{
        'title': 'Bunayya Tv (Indonesia)',
        'logo': 'livetv.jpg',
        'stream_url': ('rtmp://119.235.249.60:1935/bunayyatv/live'),
    },
	{
        'title': 'Dubai Noor (Uae)',
        'logo': 'livetv.jpg',
        'stream_url': ('http://dmivll.mangomolo.com/noordubaitv/smil:noordubaitv.smil/chunklist_b750000.m3u8'),
    },
	{
        'title': 'Islam Channel (Pakistan)',
        'logo': 'livetv.jpg',
        'stream_url': ('http://wowza04.sharp-stream.com/islamtv/islamtv/HasBahCa.m3u8'),
    },
	{
        'title': 'Muslim Tv (Thai)',
        'logo': 'livetv.jpg',
        'stream_url': ('http://radio2.thaidhost.com:8888/muslimonair2/live/playlist.m3u8'),
    },
	{
        'title': 'Peace Tv (Uk)',
        'logo': 'livetv.jpg',
        'stream_url': ('rtmp://peace.fms.visionip.tv/live/b2b-peace_sky-live-25f-4x3-sdh_1'),
    },
	{
        'title': 'Surau Tv (Indonesia)',
        'logo': 'livetv.jpg',
        'stream_url': ('http://wowza60.indostreamserver.com:1935/surautv/live/playlist.m3u8'),
    },
	{
        'title': 'Tahfidz Tv (Indonesia)',
        'logo': 'livetv.jpg',
        'stream_url': ('rtmp://119.235.249.58:1935/tahfidztv/live'),
    },
	{
        'title': 'Wesal Tv (Indonesia)',
        'logo': 'livetv.jpg',
        'stream_url': ('rtmp://119.235.249.60:1935/wesaltv/live'),
    },
	
)

YOUTUBE_CHANNELS = (
    {
        'name': '[COLOR orange]Bacaan Al-Quran 30 Juz[/COLOR]',
        'logo': 'islamicstreamstv.png',
        'channel_id': '.',
        'user': 'indiecrew',
    },
	{
        'name': 'Sheikh Mishary Rashid Alafasy',
        'logo': 'islamic1.jpg',
        'channel_id': 'PL9DE754DA1ABF407F',
        'user': 'Tariq Jamil',
    }, 
	{
        'name': 'Sheikh Saad Said Al-Ghamdi',
        'logo': 'islamic1.jpg',
        'channel_id': 'PLFBCB5C33480F350C',
        'user': 'Wady Kuantan',
    }, 
	{
        'name': '[COLOR orange]Himpunan Kuliah Agama[/COLOR]',
        'logo': 'islamicstreamstv.png',
        'channel_id': '.',
        'user': 'indiecrew',
    },
	{
        'name': 'Tuan Guru Dato Ismail Kamus',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLxah4hde1ofEqCb487dbnNJYzRZ4CdrIS',
        'user': 'Laman an nur',
    }, 
	{
        'name': 'Tuan Guru Dato Dr Haron Din',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLDEFB9CC9B2CB60BD',
        'user': 'Laman an nur',
    },
	{
        'name': 'Ustaz Don Daniyal Don Biyajid',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLxah4hde1ofGWxJvZRppqu4jt-3bvtdG2',
        'user': 'Laman an nur',
    },
	{
        'name': 'Ustaz Shukeri Najib Ab Rahim',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLxah4hde1ofH5BbB-kOSXjYR2sLegcl0z',
        'user': 'Laman an nur',
    },
	{
        'name': 'Dato Nik Muhammad Zawawi Salleh',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLxah4hde1ofGjgOadz5-DB4uWyr2JOmo3',
        'user': 'Laman an nur',
    },
	{
        'name': 'Ustaz Wadi Annuar',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLDyvHn6TJjLwOfVhr55rijmkfKIa1k9fx',
        'user': 'zonkita zonkuliah',
    },
	{
        'name': 'Ustaz Fawwaz Mohd Jan',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLDyvHn6TJjLxPFCwOobz_oaGT7symXN8w',
        'user': 'zonkita zonkuliah',
    },
	{
        'name': 'Ustaz Shamsuri Haji Ahmad',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLDyvHn6TJjLxAFrtq4VH1E6PX1YsTt03q',
        'user': 'zonkita zonkuliah',
    },
	{
        'name': 'Ustaz Shahul Hamid',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLDyvHn6TJjLxHobz1NQog9mw1O7hK44Td',
        'user': 'zonkita zonkuliah',
    },
	{
        'name': 'Ustaz Hanif Haron',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLDyvHn6TJjLzAsT4vIgmRQKKCJ2U4mXaU',
        'user': 'zonkita zonkuliah',
    },
	{
        'name': 'Ustaz Hussain Yee',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLBQbpvlXmhNq7qjGHb5QHTBuXV_0Mq93L',
        'user': 'Al-Khaadem AKYMEDIA',
    },
	{
        'name': 'Ustaz Yunus Zainal',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLBQbpvlXmhNq8QsGVmTb6yHfTgbOmSrk_',
        'user': 'Al-Khaadem AKYMEDIA',
    },
	{
        'name': 'Ustaz Ahmad Fauwaz Fadzil',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLfVZeivIZ4wBL7zcRC5eCx6pBGgfkYFYD',
        'user': 'Telaga Biru',
    },
	{
        'name': 'Datuk Dr. Hj Zahazan Mohamed',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLfVZeivIZ4wBi_y86ilKIGGx6mQ8mJXB-',
        'user': 'Telaga Biru',
    },
	{
        'name': 'Ustaz Umar Muhammad Noor',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLfVZeivIZ4wAltHpdUrMo2yafEfuoAHjB',
        'user': 'Telaga Biru',
    },
	{
        'name': 'Ustaz Azhar Idrus',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLQ6f2t-na2YyO--IhWFEjIWYvCIAVOb-0',
        'user': 'Imam Muda',
    },
	{
        'name': 'Uztaz Kazim Elias',
        'logo': 'islamic2.jpg',
        'channel_id': 'PLAVIsaqTnK98ml2NzpHai2M-xqF4Ld2kv',
        'user': 'Ceramah Islam Terbaik',
    },
)

YOUTUBE_URL ='plugin://plugin.video.youtube/playlist/%s/?page=1'

plugin = Plugin()

@plugin.route('/')
def show_root_menu():
    items = [
        {'label': _('streams'),
         'path': plugin.url_for('show_streams')},
	{'label': _('streams2'),
         'path': plugin.url_for('show_channels')},

    ]
    return plugin.finish(items)

@plugin.route('/streams/')
def show_streams():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS]
    return plugin.finish(items)

@plugin.route('/channels/')
def show_channels():
    items = [{
        'label': channel['name'],
        'thumbnail': get_logo(channel['logo']),
        'path': YOUTUBE_URL % channel['channel_id'],
    } for channel in YOUTUBE_CHANNELS]
    return plugin.finish(items)

def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)

def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id

def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()