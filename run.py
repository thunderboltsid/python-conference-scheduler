from lib.conf import Conference, Track, Talk

def test():
	conf = Conference(name="Pfeffery Times", file="events.txt", starts_at="09:00", ends_at="16:00", lunch_at="12:00", networking_at="16:30")
	conf.add_track("Track 1")
	conf.add_track("Track 2")
	conf.schedule()
	conf.list_tracks()

test()