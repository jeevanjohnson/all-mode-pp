import aiohttp
import asyncio
import time
from lb import _lb

URL_BASE = "https://akatsuki.pw/api/v1"

all_players = {}

async def add_to_cache(json: dict) -> None:
	_json = json['stats']

	all_players[(user_id := json['id'])] = [
		_json[0]['std']['pp'],
		_json[0]['taiko']['pp'],
		_json[0]['ctb']['pp'],

		_json[1]['std']['pp'],
		_json[1]['taiko']['pp'],
		_json[1]['ctb']['pp'],
		json['username'],
		_json[0]['std']['playcount'] + _json[0]['taiko']['playcount'] + _json[0]['ctb']['playcount'] + _json[0]['mania']['playcount'] + _json[1]['std']['playcount'] + _json[1]['taiko']['playcount'] + _json[1]['ctb']['playcount']
	]

	print(f"request done for userid: {user_id}!!!!")


async def get_all_user_pp(start: int, finish: int) -> None:
	async with aiohttp.ClientSession() as session:
		for userid in range(finish):
			userid += start
			if userid == finish + 1:
				break
			async with session.get(f'{URL_BASE}/users/full?id={userid}') as resp:
				if not resp or resp.status != 200 or not (json := await resp.json()):
					print(f'{userid} dont exist')
					continue

				await add_to_cache(json)
				continue

async def main():
	# get_all_user_pp(start_userid, end_userid)
	a = asyncio.create_task(get_all_user_pp(1000, 5000))
	e = asyncio.create_task(get_all_user_pp(5001, 10000))
	i = asyncio.create_task(get_all_user_pp(10001, 15000))
	o = asyncio.create_task(get_all_user_pp(15001, 20000))
	_a = asyncio.create_task(get_all_user_pp(20001, 25000))
	_e = asyncio.create_task(get_all_user_pp(25001, 30000))
	_i = asyncio.create_task(get_all_user_pp(30001, 35000))
	_o = asyncio.create_task(get_all_user_pp(35001, 40000))
	_u = asyncio.create_task(get_all_user_pp(40001, 44000))
	await a ; await e  
	await i ; await o
	await _a ; await _e
	await _i ; await _o
	await _u
	leaderboard = _lb(all_players)
	return leaderboard