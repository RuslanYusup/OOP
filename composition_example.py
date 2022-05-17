


class MusicBand:
	def __init__(self, title, label, musician = None):
		self.title = title
		self.label = label
		self.musician = musician
		self.album = []

	def write_album(self, album):
		self.album.append(album)


class Musician:
	def __init__(self, name, instrument):
		self.name = name
		self.instrument = instrument
	
	def __str__(self):
		return f"{self.name} {self.instrument}"

class Album:
	def __init__(self, song, genre):
		self.song = song
		self.genre = genre

band_1 = MusicBand("Beatles", "parlophone", "beatles")
band_1.write_album("White Album")
band_1.write_album("Hard")
band_1.write_album("Help")

print(band_1.title, band_1.musician, band_1.label, band_1.album)

	