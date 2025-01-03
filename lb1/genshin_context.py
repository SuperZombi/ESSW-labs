from enum import Enum

class Vision(Enum):
	PYRO = {"text": "Піро", "img": "vision/pyro.png"}
	HYDRO = {"text": "Гідро", "img": "vision/hydro.png"}
	ANEMO = {"text": "Анемо", "img": "vision/anemo.png"}
	ELECTRO = {"text": "Електро", "img": "vision/electro.png"}
	CRYO = {"text": "Кріо", "img": "vision/cryo.png"}
	GEO = {"text": "Гео", "img": "vision/geo.png"}

class Weapon(Enum):
	SWORD = {"text": "Одноручний меч", "img": "weapon/sword.png"}
	CLAYMORE = {"text": "Дворучний меч", "img": "weapon/claymore.png"}
	POLEARM = {"text": "Спис", "img": "weapon/polearm.png"}
	CATALYST = {"text": "Каталізатор", "img": "weapon/catalyst.png"}
	BOW = {"text": "Лук", "img": "weapon/bow.png"}
	
class Nation(Enum):
	MONDSTADT = {"text": "Мондштадт", "img": "nation/mondstadt.png"}
	LIYUE = {"text": "Ліюе", "img": "nation/liyue.png"}
	INAZUMA = {"text": "Інадзума", "img": "nation/inazuma.png"}
	SNEZHNAYA = {"text": "Сніжна", "img": "nation/snezhnaya.png"}

class Rarity(Enum):
	FOUR_STAR = {"text": "4 зірковий", "img": "star/violet.png"}
	FIVE_STAR = {"text": "5 зірковий", "img": "star/orange.png"}

class Gender(Enum):
	MALE = {"text": "Чоловік", "img": "gender/male.png"}
	FEMALE = {"text": "Жінка", "img": "gender/female.png"}
