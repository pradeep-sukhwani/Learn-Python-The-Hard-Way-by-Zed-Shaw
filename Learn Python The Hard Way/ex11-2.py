print "How many games do you have for PC? ",
pc_games = int(raw_input())
print "Name each of them: ",
pc_games_names = raw_input()

print "How many games do you have for PS4? ",
ps4_games = int(raw_input())
print "Name each of them: ",
ps4_games_names = raw_input()

print "How many games do you have for Xbox One?",
xbox_one_games = int(raw_input())
print "Name each of them: ",
xbox_one_games_names = raw_input()

print "So you have %r games of PC, %r of PS4, %r of Xbox-One" %(pc_games, ps4_games, xbox_one_games)
print "PC Games: %s" %(pc_games_names)
print "PS4 Games: %s" %(ps4_games_names)
print "Xbox-One Games: %s" %(xbox_one_games_names)