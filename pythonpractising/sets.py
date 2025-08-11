
football_players = {"Adam","Brian","Charles","Dickens","Eliud","Frank","george"}
basketball_players = {"Elias","george","Halan","ian","jackson","Charles","Dickens",}

#adding an item to the list 
football_players.add("zablon")
print("All the football players include:",football_players)

#adding players from another set we use update()
new_players = {"Odergard","paul","Queen","Roan"}

basketball_players.update(new_players)
print(" basketball players are: ",basketball_players)

basketball_players.discard("Queen")
print("the new basketball players are: ",basketball_players)
print("the players who play football are:")

for players in football_players:
    print(players)

#---------------------------------------------------SETS OPERATIONS-----------------------------------------------------
#-------UNION-----------
all_players = football_players.union(basketball_players)
print("all players in the school are :",all_players)
print(f"the players in the school are {len(all_players)} in total")

#---------intersection-----------
football_and_basketball_player = basketball_players.intersection(football_players)
print("those players who play both basketball and football are: ",football_and_basketball_player)

#-----------difference--------------------
only_football = football_players.difference(basketball_players)
print(f"the players who play only football are: {only_football} and they are {len(only_football)} in total")

only_basketball = basketball_players.difference(football_players)
print(f"players who only play basketball are {only_basketball} and they are {len(only_basketball)} in total")

#---------------symetric difference
one_sport = football_players.symmetric_difference(basketball_players)
print(f"The players who only play one sport are : {one_sport} and they are {len(one_sport)} in total")