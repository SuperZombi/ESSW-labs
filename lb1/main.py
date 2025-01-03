import eel
from knowledge_base import GenshinAkinator, Character
from genshin_context import *


def as_enum(d): return {d.name:d.value}
def flatten(data): return dict((key,d[key]) for d in data for key in d)

class ChatFSM:
	def __init__(self):
		self.state = 'START'
		self.answers = {}

	def next_state(self, user_input):
		if self.state == 'START':
			self.state = 'ASK_VISION'
			return {
				"text": "Який елемент має персонаж?",
				"options": flatten([
					as_enum(Vision.PYRO),
					as_enum(Vision.HYDRO),
					as_enum(Vision.ANEMO),
					as_enum(Vision.ELECTRO),
					as_enum(Vision.CRYO),
					as_enum(Vision.GEO)
				])
			}
		
		elif self.state == 'ASK_VISION':
			self.answers['vision'] = Vision[user_input]
			self.state = 'ASK_WEAPON'
			return {
				"text": "Яку зброю використовує персонаж?",
				"options": flatten([
					as_enum(Weapon.SWORD),
					as_enum(Weapon.CLAYMORE),
					as_enum(Weapon.POLEARM),
					as_enum(Weapon.CATALYST),
					as_enum(Weapon.BOW)
				])
			}

		elif self.state == 'ASK_WEAPON':
			self.answers['weapon'] = Weapon[user_input]
			self.state = 'ASK_NATION'
			return {
				"text": "З якої країни персонаж?",
				"options": flatten([
					as_enum(Nation.MONDSTADT),
					as_enum(Nation.LIYUE),
					as_enum(Nation.INAZUMA),
					as_enum(Nation.SNEZHNAYA)
				])
			}
		
		elif self.state == 'ASK_NATION':
			self.answers['nation'] = Nation[user_input]
			self.state = 'ASK_RARITY'
			return {
				"text": "Яка рідкість персонажа?",
				"options": flatten([
					as_enum(Rarity.FOUR_STAR),
					as_enum(Rarity.FIVE_STAR)
				])
			}
		
		elif self.state == 'ASK_RARITY':
			self.answers['rarity'] = Rarity[user_input]
			self.state = 'ASK_GENDER'
			return {
				"text": "Якої статі персонаж?",
				"options": flatten([
					as_enum(Gender.MALE),
					as_enum(Gender.FEMALE)
				])
			}
		
		elif self.state == 'ASK_GENDER':
			self.answers['gender'] = Gender[user_input]
			self.state = 'RESULT'
			return self.process_character()

	def process_character(self):
		akinator = GenshinAkinator()
		akinator.reset()
		
		character_facts = Character(
			vision=self.answers['vision'],
			weapon=self.answers['weapon'],
			nation=self.answers['nation'],
			rarity=self.answers['rarity'],
			gender=self.answers['gender']
		)
		akinator.declare(character_facts)
		akinator.run()

		if akinator.response:
			return akinator.response
		return {"text": "Нажаль я не зміг вгадати твого персонажа 😢"}


fsm = None
@eel.expose
def new_chat():
	global fsm
	fsm = ChatFSM()

@eel.expose
def process_message(user_input=""):
	response = fsm.next_state(user_input)
	return response


eel.init('web')
eel.start('index.html', size=(550,750))
