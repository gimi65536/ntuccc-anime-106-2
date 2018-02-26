from typing import List
from collections import OrderedDict
from itertools import product, combinations
total_time : int = 60
sol : List = []
max_count = 0
anime1 = [
	["高木", 24, ("Tue", "Thu", "Fri")],
	["寶石", 24, ("Tue", "Thu", "Fri")],
	["絕唱", 48, ("Tue", "Wed", "Thu", "Fri")],
	["調教", 24, ("Mon", "Tue", "Wed", "Thu", "Fri")],
	["幻想", 30, ("Wed", "Thu")]
]
anime2 = [
	["手機", 24, ("Mon",), False],
	["不正經", 24, ("Mon",), False],
	["悠哉", 48, ("Fri",), False],
	["可塑", 24, ("Wed", "Thu"), False],
	["暴坊", 46, ("Mon", "Tue", "Wed", "Thu", "Fri"), False],
	["奇諾", 24, ("Mon", "Tue", "Wed", "Thu", "Fri"), False],
	["活寶", 22, ("Mon", "Wed", "Fri"), False]
]
def pickfirst():
	x = product(*(range(len(i[2])) for i in anime1))
	for i in x:
		days = OrderedDict([(s, total_time) for s in ['Mon', "Tue", "Wed", "Thu", "Fri"]])
		for anime, day in zip(anime1, i):
			days[anime[2][day]] -= anime[1]
		if sum(i < 0 for i in days.values()):
			continue
		yield ([(anime[0], anime[2][day]) for anime, day in zip(anime1, i)], days)

def pick():
	global max_count, sol
	for l, Days in pickfirst():
		#days = Days.copy()
		for n in range(len(anime2), -1, -1):
			if n < max_count: break
			for c in combinations(range(len(anime2)), n):
				picked = list(anime2[i] for i in c)
				#print(*(i[2] for i in picked))
				x = product(*(i[2] for i in picked))
				for choose in x:
					time = list(i[1] for i in picked)
					days = Days.copy()
					#print(choose)
					for t, day in zip(time, choose):
						days[day] -= t
					if sum(i < 0 for i in days.values()):
						continue
					if n > max_count:
						max_count = n
						sol = []
					#print(l + [(anime[0], day) for anime, day in zip(picked, choose)])
					sol.append(l + [(anime[0], day) for anime, day in zip(picked, choose)])

pick()
print(*sol, sep = "\n")
