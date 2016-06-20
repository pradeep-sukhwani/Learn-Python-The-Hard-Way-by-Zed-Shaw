def no_of_games(pc_games, ps4_games, xbox_one_games):
	print "I've %d games of pc." % pc_games
	print "I've %d games of PS4." % ps4_games
	print "I've %d games of Xbox-One." % xbox_one_games
	print "I think I've a plenty of games.\n"

print "1st method: Simply calling the function."
no_of_games(10,03,93)

print "2nd method: By doing math."
no_of_games(10+10, 03+10, 93+10)

print "3rd method: By variable."
games_for_pc = 20
games_for_ps4 = 30
games_for_xbox_one = 50

no_of_games(games_for_pc,games_for_ps4,games_for_xbox_one)

print "4th method: By variable + math."
no_of_games(games_for_pc + 15, games_for_ps4 + 15, games_for_xbox_one + 15)