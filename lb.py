from calc import *

def _lb(all_players):
	new_dict = {}

	for user in all_players:
		new_dict[user] = calc_without_mania(all_players[user])

	rank = 0
	man = sorted(new_dict, key=new_dict.get, reverse=True)
	lb = ''
	for user in man:
		rank += 1
		lb += f'Rank: {rank} | User: {all_players[user][6]} | Playcount: {all_players[user][7]} | {new_dict[user]}PP\n'
	print('lb done!')
	return lb