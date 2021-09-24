# To Download Songs.
from io import BytesIO
from bot import aiohttpsession as session


async def download_song(url):
    async with session.get(url) as resp:
        song = await resp.read()
    song = BytesIO(song)
    song.name = "a.mp3"
    return song

# Needed. 
is_downloading = False
dl_limit = 0
