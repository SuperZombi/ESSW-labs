from experta import *
from genshin_context import *

class Character(Fact): pass

class GenshinAkinator(KnowledgeEngine):
	def __init__(self):
		super().__init__()
		self.response = None
	
	@Rule(Character(vision=Vision.PYRO, weapon=Weapon.CLAYMORE, nation=Nation.MONDSTADT, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def diluc(self):
		self.response = {"text": "Я думаю, що це Ділюк!", "img": "characters/diluc.jpg"}
	
	@Rule(Character(vision=Vision.ANEMO, weapon=Weapon.SWORD, nation=Nation.MONDSTADT, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def jean(self):
		self.response = {"text": "Я думаю, що це Джин!", "img": "characters/jean.jpg"}
	
	@Rule(Character(vision=Vision.HYDRO, weapon=Weapon.CATALYST, nation=Nation.MONDSTADT, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def mona(self):
		self.response = {"text": "Я думаю, що це Мона!", "img": "characters/mona.jpg"}
	
	@Rule(Character(vision=Vision.PYRO, weapon=Weapon.SWORD, nation=Nation.MONDSTADT, rarity=Rarity.FOUR_STAR, gender=Gender.MALE))
	def bennett(self):
		self.response = {"text": "Я думаю, що це Беннет!", "img": "characters/bennett.jpg"}
	
	@Rule(Character(vision=Vision.ELECTRO, weapon=Weapon.SWORD, nation=Nation.LIYUE, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def keqing(self):
		self.response = {"text": "Я думаю, що це Кецин!", "img": "characters/keqing.png"}
	
	@Rule(Character(vision=Vision.GEO, weapon=Weapon.POLEARM, nation=Nation.LIYUE, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def zhongli(self):
		self.response = {"text": "Я думаю, що це Чжунлі!", "img": "characters/zhongli.jpg"}
	
	@Rule(Character(vision=Vision.PYRO, weapon=Weapon.POLEARM, nation=Nation.LIYUE, rarity=Rarity.FOUR_STAR, gender=Gender.FEMALE))
	def xiangling(self):
		self.response = {"text": "Я думаю, що це Сянлінг!", "img": "characters/xiangling.jpg"}
	
	@Rule(Character(vision=Vision.ANEMO, weapon=Weapon.POLEARM, nation=Nation.LIYUE, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def xiao(self):
		self.response = {"text": "Я думаю, що це Сяо!", "img": "characters/xiao.jpg"}
	
	@Rule(Character(vision=Vision.CRYO, weapon=Weapon.SWORD, nation=Nation.LIYUE, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def qiqi(self):
		self.response = {"text": "Я думаю, що це Циці!", "img": "characters/qiqi.png"}
	
	@Rule(Character(vision=Vision.HYDRO, weapon=Weapon.BOW, nation=Nation.SNEZHNAYA, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def tartaglia(self):
		self.response = {"text": "Я думаю, що це Тарталья (Чайлд)!", "img": "characters/tartaglia.jpg"}
	
	@Rule(Character(vision=Vision.CRYO, weapon=Weapon.BOW, nation=Nation.LIYUE, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def ganyu(self):
		self.response = {"text": "Я думаю, що це Ганьюй!", "img": "characters/ganyu.jpg"}
	
	@Rule(Character(vision=Vision.GEO, weapon=Weapon.SWORD, nation=Nation.MONDSTADT, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def albedo(self):
		self.response = {"text": "Я думаю, що це Альбедо!", "img": "characters/albedo.png"}
	
	@Rule(Character(vision=Vision.ANEMO, weapon=Weapon.BOW, nation=Nation.MONDSTADT, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def venti(self):
		self.response = {"text": "Я думаю, що це Венті!", "img": "characters/venti.jpg"}
	
	@Rule(Character(vision=Vision.PYRO, weapon=Weapon.POLEARM, nation=Nation.LIYUE, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def hu_tao(self):
		self.response = {"text": "Я думаю, що це Хутао!", "img": "characters/hu_tao.png"}
	
	@Rule(Character(vision=Vision.ELECTRO, weapon=Weapon.POLEARM, nation=Nation.INAZUMA, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def raiden_shogun(self):
		self.response = {"text": "Я думаю, що це Райден!", "img": "characters/raiden.png"}

	@Rule(Character(vision=Vision.CRYO, weapon=Weapon.SWORD, nation=Nation.INAZUMA, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def ayaka(self):
		self.response = {"text": "Я думаю, що це Аяка!", "img": "characters/ayaka.jpg"}
	
	@Rule(Character(vision=Vision.ANEMO, weapon=Weapon.SWORD, nation=Nation.INAZUMA, rarity=Rarity.FIVE_STAR, gender=Gender.MALE))
	def kazuha(self):
		self.response = {"text": "Я думаю, що це Кадзуха!", "img": "characters/kazuha.jpg"}
	
	@Rule(Character(vision=Vision.CRYO, weapon=Weapon.CLAYMORE, nation=Nation.MONDSTADT, rarity=Rarity.FIVE_STAR, gender=Gender.FEMALE))
	def eula(self):
		self.response = {"text": "Я думаю, що це Еола!", "img": "characters/eula.jpg"}
	
	@Rule(Character(vision=Vision.ELECTRO, weapon=Weapon.BOW, nation=Nation.MONDSTADT, rarity=Rarity.FOUR_STAR, gender=Gender.FEMALE))
	def fischl(self):
		self.response = {"text": "Я думаю, що це Фішль!", "img": "characters/fischl.jpg"}
	
	@Rule(Character(vision=Vision.CRYO, weapon=Weapon.SWORD, nation=Nation.MONDSTADT, rarity=Rarity.FOUR_STAR, gender=Gender.MALE))
	def kaeya(self):
		self.response = {"text": "Я думаю, що це Кея!", "img": "characters/kaeya.png"}
