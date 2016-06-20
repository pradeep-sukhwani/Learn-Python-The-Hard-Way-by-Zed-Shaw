class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

here_we_go_again = Song(["All the time that you wasted,", 
						 "I was saving it all",
						 "Running down a lonely road", 
						 "here we go, here we go again"])

wildest_moment = Song(["You and I, bloodline,",
					   "We come together every time",
					   "Two wrongs, no rights,",
					   "We lose ourselves at night"])
					   
sweet_talker = here_we_go_again
jessie_ware = wildest_moment

sweet_talker.sing_me_a_song()
jessie_ware.sing_me_a_song()