from typing import List
from itertools import product, combinations
import random
total_time : int = 60
anime1 : List = [
	["擅長捉弄人的高木同學"     , 24, ("Tue", "Thu", "Fri")],
	["寶石之國"               , 24, ("Tue", "Thu", "Fri")],
	["戰姬絕唱"               , 48, ("Tue", "Wed", "Thu", "Fri")],
	["調教咖啡廳"             , 24, ("Mon", "Tue", "Wed", "Thu", "Fri")],
	["幻想萬華鏡"             , 30, ("Wed", "Thu")]
]
anime2 : List = [
	["帶著智慧型手機闖蕩異世界"  , 24, ("Mon", )],
	["不正經的魔術講師與禁忌教典", 24, ("Mon", )],
	["悠悠哉哉少女日和"        , 48, ("Fri", )],
	["可塑性記憶"             , 24, ("Wed", "Thu")],
	["暴れん坊将軍"            , 46, ("Mon", "Tue", "Wed", "Thu", "Fri")],
	["奇諾之旅2"              , 24, ("Mon", "Tue", "Wed", "Thu", "Fri")],
	["探險活寶"               , 22, ("Mon", "Wed", "Fri")]
]
def pick(animelist):
	x = product(*(range(len(i[2])) for i in animelist))
	for i in x:
		days = {s: total_time for s in ["Mon", "Tue", "Wed", "Thu", "Fri"]}
		for anime, day in zip(animelist, i):
			days[anime[2][day]] -= anime[1]
		if sum(i < 0 for i in days.values()):
			continue
		yield [(anime[0], anime[2][day]) for anime, day in zip(animelist, i)]

if __name__ == "__main__":
	sol : List = anime1.copy()
	plan : List = []
	print("必然選上之作品有:", *('\"' + anime[0] + '\"' for anime in anime1))
	sd = input("請輸入種子碼: ")
	random.seed(sd) #以字串為種子碼
	print("設置種子為: {}".format(sd))
	order = random.sample(range(len(anime2)), len(anime2))
	print("現在選中的作品隨機排序為:", *('\"' + anime2[i][0] + '\"' for i in order))
	for i in order:
		anime = anime2[i] #選中一個作品
		print("現在選中作品: {}".format(anime[0]))
		l = [p for p in pick(sol + [anime])]
		if len(l) == 0: #時間塞不下去的話則跳過
			print("塞不下去...")
			continue
		print("塞得下去!!!")
		sol = sol + [anime] #時間塞得下去的話就取代原本的方案
		plan = l
		print("現在選中的作品有:", *('\"' + anime[0] + '\"' for anime in sol))
	#以本次例子來講，特定一個一次播放24分鐘的番被選中的機率是1/21 * 0 + 2/3 * 2/5 + 2/7 * 4/5 = 4/7 = 57%
	#而一次播放40分鐘以上的一個番被選中的機率為1/21 * 1 + 2/3 * 1/2 + 2/7 * 0 = 8/21 = 38%
	print("\n於是，現在選中的作品有: ", *('\"' + anime[0] + '\"' for anime in sol))
	print("有{}種播放日期的排法".format(len(plan)))
	choose = random.randint(0, len(plan))
	print("\n選中的排法為:")
	for name, day in plan[choose]:
		print('\t\"{}\" {}'.format(name, day))
	print()
	#現在決定某一天內播放的時間先後順序
	for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
		anime = [i[0] for i in plan[choose] if i[1] == day]
		print("{} 有這些動畫:".format(day), *('\"' + a + '\"' for a in anime))
		random.shuffle(anime)
		print("\t隨機排序後的播放順序:".format(day), *('\"' + a + '\"' for a in anime))
	print("\n選擇完畢，之後將由本人手動填充那些票數更低但播放時間短的作品進去...")