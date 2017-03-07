from beets.plugins import BeetsPlugin

class KodiNfo(BeetsPlugin):
  def __init__(self):
    super(KodiNfo, self).__init__()
    self.register_listener('album_imported', self.makeAlbumNfo)

  def makeAlbumNfo(self, lib, album):
    file = open(album.path + "/album.nfo","w+")
    file.write("https://musicbrainz.org/release/%s" % album.mb_albumid)
    file.close()