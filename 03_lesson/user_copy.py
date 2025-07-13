class User: #класс

	def __init__(self, first_name, last_name): #конструктор
		print("данные приняты и зарегестрированны")
		self.firname = first_name #поле класса Имя
		self.lastname = last_name  #поле класса Фамилия

	def sayfirst_name(self): #метод ИМЯ
		print("меня зовут ", self.firname)

	def saylast_name(self): #метод ФАМИЛИЯ
		print("моя фамилия ", self.lastname) 

	def sayfull_name(self): #метод Полное имя
		print("Приятно познакомиться ", self.firname, self.lastname)
	
