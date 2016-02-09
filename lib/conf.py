class Talk(object):
	"""docstring for Talk"""
	def __init__(self, title="Generic Talk", duration=0):
		super(Talk, self).__init__()
		self.title = title
		self.duration = duration


class Track(object):
	"""docstring for Track"""
	def __init__(self, name, starts_at=None, lunch_at=None, networking_at=None):
		super(Track, self).__init__()
		self.name = name
		self.starts_at = starts_at
		self.lunch_at = lunch_at
		self.networking_at = networking_at
		self.talks = []

	def add_talk(talk):
		self.talks.append(talk)


class Conference(object):
	"""docstring for Conference"""
	def __init__(self, name="Generic Conference", file=None):
		super(Conference, self).__init__()
		self.name = name
		self.tracks = []
		self.unassigned_talks = []
		if file:
			parse_file()

	def parse_file():
		inp = open(file, 'r')
		line = inp.readline()
		while line:
			inp_array = line.split()
			if inp_array[len(inp_array)-1]=="lightning":
				duration = 5
			else:
				duration = str(inp_array[len(inp_array)-1][:-3])
			name = " ".join(inp_array[:len(inp_array)-1])
			self.unassigned_talks.append(Talk(name=name, duration=duration))
			line = inp.readline()

	def add_track(self, name):
		self.tracks.append(Track(name))

	def list_tracks(self):
		print [track.name for track in self.tracks]

	def add_talk(name, duration):
		self.unassigned_talks.append(Talk(name, duration))

	def schedule(self):
		for track in self.tracks:


def test():
	conf = Conference(name="Pfeffery Times")
	conf.add_track("Track 1")
	conf.add_track("Track 2")
	conf.list_tracks()

# test()
