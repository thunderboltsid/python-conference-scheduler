from time import strptime, strftime

class Talk(object):
	"""docstring for Talk"""
	def __init__(self, title="Generic Talk", duration=60, starts_at=None):
		super(Talk, self).__init__()
		self.title = title
		self.duration = duration
		self.starts_at = starts_at


class Track(object):
	"""docstring for Track"""
	def __init__(self, name, starts_at=None, ends_at=None, lunch_at=None, networking_at=None):
		super(Track, self).__init__()
		self.name = name
		self.starts_at = starts_at
		self.ends_at = ends_at
		self.lunch_at = lunch_at
		self.networking_at = networking_at
		self.talks = []

	def add_talk(self, talk):
		self.talks.append(talk)

	def schedule(self, start, end, talks):
		start_min = start.tm_hour * 60 + start.tm_min
		end_min = end.tm_hour * 60 + end.tm_min
		length = end_min - start_min
		current_length = 0
		for index, talk in enumerate(talks):
			if current_length < length and current_length + talk.duration <= length:
				talk.starts_at = strptime(str(start.tm_hour + current_length / 60) + ":" + str(current_length%60), "%H:%M")
				self.talks.append(talk)
				talks.pop(index)
				current_length += talk.duration
		return talks


class Conference(object):
	"""docstring for Conference"""
	def __init__(self, name="Generic Conference", file=None, starts_at=None, ends_at=None, lunch_at=None, networking_at=None):
		super(Conference, self).__init__()
		self.name = name
		self.tracks = []
		self.unassigned_talks = []
		self.starts_at = strptime(starts_at, "%H:%M")
		self.ends_at = strptime(ends_at, "%H:%M")
		self.lunch_at = strptime(lunch_at, "%H:%M")
		self.networking_at = strptime(networking_at, "%H:%M")
		if file:
			self.parse_file(file)

	def parse_file(self, file):
		inp = open(file, 'r')
		line = inp.readline()
		while line:
			inp_array = line.split()
			if inp_array[len(inp_array)-1]=="lightning":
				duration = 5
			else:
				duration = int(inp_array[len(inp_array)-1][:-3])
			title = " ".join(inp_array[:len(inp_array)-1])
			self.unassigned_talks.append(Talk(title=title, duration=duration))
			line = inp.readline()

	def add_track(self, name):
		self.tracks.append(Track(name, starts_at=self.starts_at, ends_at=self.ends_at, lunch_at=self.lunch_at, networking_at=self.networking_at))

	def list_tracks(self):
		for track in self.tracks:
			print track.name + ":"
			for talk in track.talks:
				print strftime("%I:%M %p", talk.starts_at) + " " + talk.title

	def add_talk(name, duration):
		self.unassigned_talks.append(Talk(name, duration))

	def schedule(self):
		for track in self.tracks:
			self.unassigned_talks = track.schedule(self.starts_at, self.lunch_at, self.unassigned_talks)
			track.add_talk(Talk(title="Lunch", starts_at=self.lunch_at))
			self.unassigned_talks = track.schedule(strptime(str(self.lunch_at.tm_hour + 1) + ":" + str(self.lunch_at.tm_min), "%H:%M"), self.ends_at, self.unassigned_talks)
			track.add_talk(Talk(title="Netowrking Event", starts_at=self.networking_at))

